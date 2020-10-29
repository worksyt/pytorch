# -*- config:utf-8 -*-
"""
作者:计AI181宋曜通 201806030121
日期：2020年10月27日
"""
import numpy as np
from os import listdir  # 使用listdir模块，用于访问本地文件
from sklearn.neural_network import MLPClassifier


def img2vector(file_name):
    """
    将加载的32*32的图片矩阵展开成一维向量。
    :param file_name: 文件路径
    :return: retMat: 一维向量
    """
    retMat = np.zeros([1024], int)  # 定义返回的矩阵，大小为1*1024
    fr = open(file_name)  # 打开包含32*32大小的数字文件
    lines = fr.readlines()  # 读取文件的所有行
    for i in range(32):  # 遍历文件所有行
        for j in range(32):  # 并将01数字存放在retMat中
            retMat[i * 32 + j] = lines[i][j]
    return retMat


def read_dataset(path):
    """
    加载训练数据，并将样本标签转化为one-hot向量
    :param path: 文件夹路径
    :return: data_set, hw_labels: 训练数据, 标签数据
    """
    file_list = listdir(path)  # 获取文件夹下的所有文件
    num_files = len(file_list)  # 统计需要读取的文件的数目
    data_set = np.zeros([num_files, 1024], int)  # 用于存放所有的数字文件
    hw_labels = np.zeros([num_files, 10])  # 用于存放对应的one-hot标签
    for file in range(num_files):  # 遍历所有的文件
        file_path = file_list[file]  # 获取文件名称/路径
        digit = int(file_path.split('_')[0])  # 通过文件名获取标签
        hw_labels[file][digit] = 1.0  # 将对应的one-hot标签置1
        data_set[file] = img2vector(path + '/' + file_path)  # 读取文件内容
    return data_set, hw_labels


if __name__ == "__main__":
    '''加载训练数据'''
    train_dataSet, train_hwLabels = read_dataset('D:\pycharm\PycharmProject\pytorch\ku\\trainingDigits')

    '''训练神经网络'''
    '''
    隐藏层：一层，含100个神经元
    激活函数：logistic
    优化方法：adam
    学习率：0.0001
    最大迭代次数：2000
    '''
    clf = MLPClassifier(hidden_layer_sizes=(100,),
                        activation='logistic', solver='adam',
                        learning_rate_init=0.0001, max_iter=20000)
    print(clf)
    # fit函数能够根据训练集及对应标签集自动设置多层感知机的输入与输出层的神经元个数
    clf.fit(train_dataSet, train_hwLabels)

    '''加载测试数据'''
    dataSet, hwLabels = read_dataset('D:\pycharm\PycharmProject\pytorch\ku\\testDigits')
    '''预测并计算错误率'''
    res = clf.predict(dataSet)  # 对测试集进行预测
    error_num = 0  # 统计预测错误的数目
    num = len(dataSet)  # 测试集的数目
    for i in range(num):  # 遍历预测结果
        # 比较长度为10的数组，返回包含01的数组，0为不同，1为相同
        # 若预测结果与真实结果相同，则10个数字全为1，否则不全为1
        if np.sum(res[i] == hwLabels[i]) < 10:
            error_num += 1
    print("Total num:", num, " Wrong num:",
          error_num, "  WrongRate:", error_num / float(num))
