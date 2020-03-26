# coding:utf-8
"""
NLP 自然语言学习
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import math, operator

# 中文乱码
# myfont = fm.FontProperties(fname='C:\Windows\Fonts\simsunb.ttf')  # 只支持后缀ttc
# plt.rcParams['font.sans-serif'] = ['SimHei']

"数据保存到文件中"


def create_dataset():
    datasets = np.array([[8, 4, 2], [7, 1, 1, ], [1, 4, 4], [3, 0, 5]])  # 数据集
    labels = ['非常热', '非常热', '一般热', '一般热']  # 类标签
    return datasets, labels


def create_datasets():
    datasets = np.array([[8, 4, 2], [7, 1, 1, ], [1, 4, 4], [3, 0, 5], [3, 0, 4], [5, 2, 1], [5, 3, 2]])  # 数据集
    labels = [0, 0, 1, 1, 0, 0, 1]  # ['非常热','非常热','一般热','一般热','一般热']                     # 类标签
    return datasets, labels


"可视化分析数据"


def analyze_data_plot(x, y):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(x, y)
    # plt.scatter(x,y)
    # 设置散点图标题和横坐标
    # plt.title('冷热感知图',fontsize=25,fontproperties=myfont)
    plt.title('冷热感知图', fontsize=25)
    # plt.xlabel('冰淇淋',fontsize=15,fontproperties=myfont)
    plt.xlabel('冰淇淋', fontsize=15)
    # plt.ylabel('喝水', fontsize=15, fontproperties=myfont)
    plt.ylabel('喝水', fontsize=15)
    # 自动保存
    plt.savefig('result.png', bbox_inches='tight')
    plt.show()


"构造KNN分类器"


def knn_classifier(newV, datasets, labels, k):
    # 1.计算样本数据和样本库数据的距离
    sqrtDist = EuclideanDis3(newV, datasets)
    # 2.根据距离排序,按照列向量排序
    sortedDistIndexs = sqrtDist.argsort(axis=0)

    # 3.针对k个值，统计各个类别的数量
    classCount = {}
    for i in range(k):
        # 根据距离排序，索引值找到类标签
        votelabel = labels[sortedDistIndexs[i]]
        # 统计类标签的键值对
        classCount[votelabel] = classCount.get(votelabel, 0) + 1

    # 4.投票机制，少数服从多数原则
    # 对各个分类字典进行排序，降序，按照值
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
    # print('结果预测：',sortedClassCount[0][0])
    return sortedClassCount[0][0]


"欧式距离计算 d2=(x1-x2)2+(y1-y2)2"


def computeEuclideanDis(x1, x2, y1, y2):
    d = math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2))
    return d


"欧式距离计算优化公式"


def EuclideanDis(instance1, instance2):
    d = 0
    length = len(instance1)
    for x in range(length):
        d += math.pow(instance1[x] - instance2[x], 2)

    return math.sqrt(d)


"欧式距离计算3:大量数据计算"


def EuclideanDis3(newV, datasets):
    # 获取向量维度
    rowsize, colsize = datasets.shape
    # 各特征向量间做差值
    diffMat = np.tile(newV, (rowsize, 1)) - datasets
    # 差值平方
    sqDiffMat = diffMat ** 2
    # 差值开方求和
    sqrtDist = sqDiffMat.sum(axis=1) ** 0.5

    return sqrtDist


"利用KNN随机预测访客天气感知度"


def predict_temperature():
    # 创建数据集和类标签
    datasets, labels = create_dataset()
    newV = [2, 4, 4]
    iceCream = float(input("Q:请问你今天吃了几个冰淇淋？\n"))
    drinkWater = float(input("Q:请问你今天喝了几瓶水？\n"))
    playHours = float(input("Q:请问你今天在户外玩了几个小时?\n"))
    newV = np.array([iceCream, drinkWater, playHours])

    # vecs = np.array([[2, 4, 4], [3, 0, 0], [5, 7, 2]])
    # for i in vecs:
    res = knn_classifier(newV, datasets, labels, 3)
    print('KNN天气预测结果', res)


"使用机器学习库sklearn实现预测"

from sklearn import neighbors


def knn_sklearn_predict():
    # 调用机器学习库knn分类器算法
    knn = neighbors.KNeighborsClassifier()
    datasets, labels = create_datasets()
    # 传入参数，特征数据和分类标签
    print(datasets)
    knn.fit(datasets, labels)
    # knn预测
    predictRes = knn.predict([[2, 4, 0]])
    print("天气：\t", "非常热" if predictRes[0] == 0 else '一般热')

    return predictRes


if __name__ == '__main__':
    # predict_temperature()
    knn_sklearn_predict()
