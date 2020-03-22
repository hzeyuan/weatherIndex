from weatherIndex.config import *


# 判断范围
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
                # print(range_obj, index)
                return index
    return 0


def get_txt(txt, params):
    output = ""
    for t in txt.keys():
        if params in range(*t):
            output = txt[t]
            break
    return output


class weatherIndex():
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
        self.windpower = kwargs.get("windpower", None)
        self.humidity = kwargs.get("humidity", None)
        self.range_temperature = kwargs.get("range_temperature", None)

    def get_lifestyle(self):
        lifestyle = [self.get_comf(), self.get_drsg(), self.get_flu(), self.get_sport(), self.get_trav(), self.get_uv(),
                     self.get_air(), self.get_cw()]
        return lifestyle

    def get_comf(self):
        weather_level = 0
        comf = ["舒适", "较舒适", "较不舒适", "很不舒适"]
        comf_level = check_range(self.temp, *comf_section)
        for index, weather_list in enumerate(weather_section):
            if self.weather in weather_list:
                weather_level = index
                break
        ret_level = (weather_level + comf_level) // 2
        txt = weather_txt[self.weather] + "," + get_txt(temperature_txt, self.temp) + "，" + get_txt(windpower_txt,
                                                                                                    self.windpower) + "，" + get_txt(
            comf_txt,
            ret_level)
        return {"type": "comf", "brf": comf[ret_level], "txt": txt}

    def get_drsg(self):
        drsg = ["炎热", "热", "舒适", "较舒适", "冷", "较冷", "寒冷"]
        temp_level = check_range(self.temp, *drsg_section)
        return {"type": "drsg", "brf": drsg[temp_level], "txt": get_txt(drsg_txt, temp_level)}

    def get_flu(self):
        flu = ["少发", "较易发", "易发", "极易发"]
        level = check_range(self.range_temperature, *flu_section)
        txt = get_txt(range_temperature_txt, self.range_temperature)
        return {"type": "flu", "brf": flu[level], "txt": txt}

    def get_sport(self):
        sport = ["适宜", "较适宜", "较不宜", "不宜"]
        winpower_level = check_range(self.windpower, *sport_section)
        for index, weather_list in enumerate(weather_section):
            if self.weather in weather_list:
                weather_level = index
                break
        ret_level = (weather_level + winpower_level) // 2
        txt = weather_txt[self.weather] + "，" + get_txt(windpower_txt, self.windpower) + "，" + get_txt(sport_txt,
                                                                                                       ret_level)
        return {"type": "sport", "brf": sport[ret_level], "txt": txt}

    def get_trav(self):
        travel = ["适宜", "较适宜", "一般", "较不宜"]
        winpower_level = check_range(self.windpower, *sport_section)
        for index, weather_list in enumerate(weather_section):
            if self.weather in weather_list:
                weather_level = index
                break
        ret_level = (weather_level + winpower_level) // 2
        txt = weather_txt[self.weather] + "，" + get_txt(windpower_txt, self.windpower) + "，" + get_txt(trav_txt,
                                                                                                       ret_level)
        return {"type": "trav", "brf": travel[ret_level], "txt": txt}

    def get_uv(self):
        weather_level = 0
        uv = ["很强", "强", "中等", "弱", "最弱"]
        uv_section = (([26, 99]), ([17, 26]), ([10, 17]), ([5, 10]), ([0, 5]))
        for index, weather_list in enumerate(weather_section):
            if self.weather in weather_list:
                weather_level = index
        temp_level = check_range(self.temp, *uv_section)
        ret_level = (weather_level + temp_level) // 2
        return {"type": "uv", "brf": uv[ret_level], "txt": get_txt(uv_txt, ret_level)}

    def get_air(self):
        air = ["优", "良", "中", "较差"]
        weather_level = 0
        for index, weather_list in enumerate(weather_section):
            if self.weather in weather_list:
                weather_level = index
        return {"type": "air", "brf": air[weather_level], "txt": get_txt(air_txt, weather_level)}

    def get_cw(self):
        cw = ["适宜", "较适宜", "一般", "较不宜"]
        weather_level = 0
        for index, weather_list in enumerate(weather_section):
            if self.weather in weather_list:
                weather_level = index
        txt = weather_txt[self.weather] + "，" + get_txt(windpower_txt, self.windpower) + "，" + get_txt(cw_txt,
                                                                                                       weather_level)
        return {"type": "cw", "brf": cw[weather_level], "txt": txt}

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


if __name__ == '__main__':
    w = weatherIndex(temp=40, windpower=3, weather="沙尘", humidity=50, range_temperature=6)
    print(w.get_lifestyle())
    print(w.get_comf())
