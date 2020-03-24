from weatherIndex.demo import WeatherIndex

if __name__ == '__main__':
    w = WeatherIndex(temp=20, windpower=4, range_temperature=8, weather="晴")
    print(w.get_lifestyle())
