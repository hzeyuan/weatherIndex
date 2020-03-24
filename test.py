from weatherIndex.demo import WeatherIndex

if __name__ == '__main__':
    w = WeatherIndex(temp=0, windpower=0, range_temperature=0, weather="晴")
    print(w.get_lifestyle())
