import difflib

from .config import *
from typing import Union, List, Tuple


def get_txt(txt, params):
    output = ""
    for t in txt.keys():
        if params in range(*t):
            output = txt[t]
            break
    else:
        output = "123"
    return output


class WeatherIndex:
    def __init__(self, **kwargs):
        """

        :param kwargs:
        temp:温度
        weather:天气
        windpower:风力指数
        humidity:湿度
        range_temperature:温差
        """
        self.temp = kwargs.get("temp", None)
        self.weather = kwargs.get('weather', None)
        if self.weather:
            weather_list = []
            for w in weather_section:
                weather_list += w
            fuzzy_weather = difflib.get_close_matches(self.weather, weather_list, 1, cutoff=0.2)
            if fuzzy_weather:
                self.weather = fuzzy_weather[0]
        else:
            self.weather = "晴"
        # 对天气进行处理，匹配一个近似值
        self.windpower = float(kwargs.get("windpower", None))
        self.humidity = float(kwargs.get("humidity", None))
        self.range_temperature = float(kwargs.get("range_temperature", None))

    def get_lifestyle(self):
        lifestyle = [self.get_comf(self.temp, self.weather),
                     self.get_drsg(self.temp),
                     self.get_flu(self.range_temperature),
                     self.get_sport(self.windpower, self.weather),
                     self.get_trav(self.windpower, self.weather),
                     self.get_uv(self.temp, self.weather),
                     self.get_air(self.weather),
                     self.get_cw(self.windpower, self.weather)]
        return lifestyle

    def get_comf(self, temp, weather):
        comf = ["舒适", "较舒适", "较不舒适", "很不舒适"]
        comf_index = self.check_range(temp, *comf_section)
        weather_index = self._get_weather_index(weather)
        ret_level = (weather_index + comf_index) // 2
        txt = '，'.join([weather_txt[self.weather],
                        get_txt(temperature_txt, temp),
                        get_txt(windpower_txt, self.windpower),
                        get_txt(comf_txt, ret_level)])
        return {"type": "comf", "brf": comf[ret_level], "txt": txt}

    def get_drsg(self, temp: Union[int, float]):
        drsg = ["炎热", "热", "舒适", "较舒适", "冷", "较冷", "寒冷"]
        temp_index = self.check_range(temp, *drsg_section)
        return {"type": "drsg", "brf": drsg[temp_index], "txt": get_txt(drsg_txt, temp_index)}

    def get_flu(self, range_temperature: Union[int, float]):
        flu = ["少发", "较易发", "易发", "极易发"]
        flu_index = self.check_range(range_temperature, *flu_section)  # 感冒指数
        txt = get_txt(range_temperature_txt, range_temperature)  # 根据温差获取文本
        return {"type": "flu", "brf": flu[flu_index], "txt": txt}

    def get_sport(self, windpower: Union[int, float], weather: str):
        sport = ["适宜", "较适宜", "较不宜", "不宜"]
        windpower_index = self.check_range(windpower, *sport_section)
        weather_index = self._get_weather_index(weather)
        ret_level = (weather_index + windpower_index) // 2
        txt = '，'.join([weather_txt[self.weather],
                        get_txt(windpower_txt, windpower),
                        get_txt(sport_txt, ret_level),
                        ])
        return {"type": "sport", "brf": sport[ret_level], "txt": txt}

    def get_trav(self, windpower: Union[int, float], weather: str):
        travel = ["适宜", "较适宜", "一般", "较不宜"]
        winpower_level = self.check_range(windpower, *sport_section)
        weather_index = self._get_weather_index(weather)
        ret_level = (weather_index + winpower_level) // 2
        txt = '，'.join([weather_txt[self.weather],
                        get_txt(windpower_txt, windpower),
                        get_txt(trav_txt, ret_level),
                        ])
        return {"type": "trav", "brf": travel[ret_level], "txt": txt}

    def get_uv(self, temp: Union[int, float], weather: str):
        uv = ["很强", "强", "中等", "弱", "最弱"]
        uv_section = (([26, 99]), ([17, 26]), ([10, 17]), ([5, 10]), ([0, 5]))
        weather_index = self._get_weather_index(weather)
        temp_index = self.check_range(temp, *uv_section)
        ret_level = (weather_index + temp_index) // 2
        return {"type": "uv", "brf": uv[ret_level], "txt": get_txt(uv_txt, ret_level)}

    def get_air(self, weather: str):
        air = ["优", "良", "中", "较差"]
        weather_index = self._get_weather_index(weather)
        return {"type": "air", "brf": air[weather_index], "txt": get_txt(air_txt, weather_index)}

    def get_cw(self, windpower: Union[int, float], weather: str):
        cw = ["适宜", "较适宜", "一般", "较不宜"]
        weather_index = self._get_weather_index(weather)
        txt = '，'.join([weather_txt[self.weather], get_txt(windpower_txt, windpower), get_txt(cw_txt, weather_index)])
        return {"type": "cw", "brf": cw[weather_index], "txt": txt}

    @staticmethod
    def _get_weather_index(weather: str):
        """获取天气指数"""
        for index, weather_list in enumerate(weather_section):
            if weather in weather_list:
                weather_index = index
                break
        else:
            weather_index = 0
        return weather_index

    # 判断范围
    @staticmethod
    def check_range(params, *args):
        """
        :param params: 接收一个判断的参数
        :param args: 接收一个温度区间
        :param kwargs:
        :return:
        """
        for index, section in enumerate(args):
            try:
                range_list = [range(*section)]
            except TypeError:
                range_list = [range(*s) for s in section]
            for range_obj in range_list:
                if params in range_obj:
                    return index
        return 0
