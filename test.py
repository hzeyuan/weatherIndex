from weatherIndex.demo import WeatherIndex
from weatherIndex.config import *
import difflib

if __name__ == '__main__':
    w = WeatherIndex(temp=27, windpower=3.0, range_temperature=5,humidity=68.0, weather="多云")
    print(w.get_lifestyle())
    #weather_list = []
    # for w in weather_section:
    #     weather_list += w
    # print(weather_list)
    # a = difflib.get_close_matches('小阵雪', weather_list, 1, cutoff=0.2)

    #a = difflib.get_close_matches('雨', weather_list, 1, cutoff=0.7)
    # print(a)
