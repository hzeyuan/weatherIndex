"""
各个指数区间
comf_section:温度区间:温度
drsg_section:穿衣区间：温度
flu_section:感冒指数区间:温差
sport_section:运动区间:风力
weather_section:天气等级区间
"""

comf_section = (([15, 25]), ([10, 15], [15, 30]), ([5, 10], [30, 32], [-5, 5]), ([32, 99], [-99, -5]))  # 舒适的温度区间
drsg_section = (([35, 99]), ([28, 35]), ([22, 28]), ([15, 22]), ([-10, 15]), ([-99, 0]))  # 穿衣的温度区间
flu_section = (([0, 13]), ([13, 15],), ([18, 99]))  # 感冒的温差区间
sport_section = (([0, 3]), ([3, 6],), ([6, 13]))  # 运动的风力区间
weather_section = (["晴", "多云", "阴"], ["轻度雾霾", "小雨", "雾", "小雪"], ["中度雾霾", "中雨", "中雪", "浮尘", "大风"],
                   ["重度雾霾", "大雨", "暴雨", "大雪", "暴雪", "沙尘"])  # 天气区间
# 天气文本
weather_txt = {
    "晴": "今天天气晴好",
    "阴": "今天，天气阴",
    "小雨": "今日可能会有小雨",
    "中雨": "今天可能会有雨水",
    "大雨": "今日可能会有大雨",
    "暴雨": "今日可能会有暴雨",
    "多云": "今天多云",
    '雾': "今天会有雾出现",
    "小雪": "今天可能会下小雪",
    "中雪": "今天降雪量较大",
    "大雪": "今天降雪量很大",
    "暴雪": "今日会有暴雪",
    "轻度雾霾": "今日有轻度雾霾",
    "中度雾霾": "今日雾霾较大",
    "重度雾霾": "今日雾霾严重",
    "浮尘": "今日沙尘较多，可见度不高",
    "大风": '今日风力很大',
    "沙尘": "今日沙尘较多，可见度不高"
}
# 温度的文本
temperature_txt = {
    (18, 25): "温度适宜",
    (25, 35): "偏热",
    (35, 99): "非常热",
    (10, 18): "偏凉",
    (0, 10): "有点冷",
    (-20, 0): "十分寒冷"
}
# 风力的文本
windpower_txt = {
    (0, 2): "无风",
    (3, 4): "有轻微的软风",
    (5, 6): "风力偏强",
    (7, 10): "风力超强"
}
# 温差的文本
range_temperature_txt = {
    (-10, 5): "昼夜温差很小，无明显降温过程，发生感冒机率很低。",
    (6, 15): "昼夜温差不大，发生感冒机率较低。",
    (16, 20): "昼夜温差较大，请注意适当增加衣服。",
    (21, 24): "昼夜温差很大，注意防寒，小心感冒。",
    (25, 30): "昼夜温差极大，极易发生感冒，请特别注意增减衣服保暖防寒。",
}

# 舒适度文本
comf_txt = {
    (0, 1): "十分舒适",
    (1, 2): "较为舒适",
    (2, 3): "较不舒适",
    (3, 4): "不是很舒适"
}
# 穿衣指数文本
drsg_txt = {
    (0, 1): '天气炎热，建议着短衫、短裙、短裤、薄型T恤衫等清凉夏季服装。',
    (1, 2): '天气热，建议着短裙、短裤、短薄外套、T恤等夏季服装。',
    (2, 3): '建议着长袖T恤、衬衫加单裤等服装。年老体弱者宜着针织长袖衬衫、马甲和长裤。',
    (3, 4): '建议着薄外套、开衫牛仔衫裤等服装。年老体弱者应适当添加衣物，宜着夹克衫、薄毛衣等。',
    (4, 5): '建议着厚外套加毛衣等服装。年老体弱者宜着大衣、呢外套加羊毛衫。',
    (5, 6): '天气冷，建议着棉服、羽绒服、皮夹克加羊毛衫等冬季服装。年老体弱者宜着厚棉衣、冬大衣或厚羽绒服。',
    (6, 7): '天气寒冷，建议着厚羽绒服、毛皮大衣加厚毛衣等隆冬服装。年老体弱者尤其要注意保暖防冻。',
}
# 运动指数文本
sport_txt = {
    (0, 1): "适合外出运动",
    (1, 2): "可以进行适当的外出活动",
    (2, 3): "建议室内活动",
    (3, 4): "天气状况不佳，不建议外出活动"
}
# 旅行指数文本
trav_txt = {
    (0, 1): "适合外出旅行",
    (1, 2): "可以在附近走动",
    (2, 3): "建议不外出游玩",
    (3, 4): "天气状况不佳，不建议外出活动"
}
# 辐射指数文本
uv_txt = {
    (0, 1): "紫外线辐射强，建议涂擦SPF20左右、PA++的防晒护肤品。避免在10点至14点暴露于日光下。",
    (1, 2): "属中等强度紫外线辐射天气，建议涂擦SPF高于15、PA+的防晒护肤品，戴帽子、太阳镜。",
    (2, 3): "紫外线强度较弱，建议涂擦SPF在12-15之间、A+的防晒护肤品。",
    (3, 4): "属弱紫外线辐射天气，无需特别防护。若长期在户外，建议涂擦SPF在8-12之间的防晒护肤品。"
}
# 空气指数文本
air_txt = {
    (0, 1): '气象条件非常有利于空气污染物稀释、扩散和清除，可在室外正常活动。',
    (1, 2): "气象条件有利于空气污染物稀释、扩散和清除，可在室外正常活动。",
    (2, 3): "气象条件对空气污染物稀释、扩散和清除无明显影响。",
    (3, 4): "气象条件较不利于空气污染物稀释、扩散和清除，请适当减少室外活动时间。"
}
# 洗车指数文本
cw_txt = {
    (0, 1): "适合洗车",
    (1, 2): "洗的车，可以保持一天整洁",
    (2, 3): "较不适合洗车",
    (3, 4): "不是很舒适洗车"
}
