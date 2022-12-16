# -*- coding:utf-8 -*-
"""
作者：hp
日期：2022年 12月10日
"""

import xlrd
import numpy as np
from itertools import combinations
##把需要转化的xlsx文件放在pycharm项目文件目录里
import pandas as pd


def preprocessPatientDataHarshly(flag=1):
    initialData = pd.read_csv(
        "ProcessedData/patient.csv",
        encoding='utf-8',
        sep=',')
    initialData = initialData.values
    keyAttr = ['Gender', 'Air Pollution', 'Alcohol use', 'Dust Allergy', 'OccuPational Hazards', 'Genetic Risk',
               'chronic Lung Disease', 'Imbalanced Diet', 'Obesity', 'Smoking', 'Passive Smoker',
               'Chest Pain', 'Coughing of Blood', 'Fatigue', 'Weight Loss', 'Shortness of Breath', 'Wheezing',
               'Swallowing Difficulty', 'Clubbing of Finger Nails', 'Frequent Cold', 'Dry Cough', 'Snoring', 'Cancered']
    print("这里是粗略处理")
    # print(initialData)
    length = len(keyAttr)
    pData = []
    for item in initialData:
        tmp = []
        for i in range(length):
            if item[i]:
                tmp.append(keyAttr[i])
        pData.append(tmp)
        # print(tmp, '\n')
    processedData = {}
    for i in range(len(pData)):
        processedData[i] = pData[i]

    return processedData


def preprocessPatientDataMoreDetailedly(flag=1):
    initialData = pd.read_csv(
        "../ProcessedData/patient2.csv",
        encoding='utf-8',
        sep=',')
    initialData = initialData.values
    keyAttr = ['Age', 'Gender', 'Air Pollution', 'Alcohol use', 'Dust Allergy', 'OccuPational Hazards', 'Genetic Risk',
               'chronic Lung Disease', 'Imbalanced Diet', 'Obesity', 'Smoking', 'Passive Smoker',
               'Chest Pain', 'Coughing of Blood', 'Fatigue', 'Weight Loss', 'Shortness of Breath', 'Wheezing',
               'Swallowing Difficulty', 'Clubbing of Finger Nails', 'Frequent Cold', 'Dry Cough', 'Snoring', 'Cancered']

    # print(initialData)
    length = len(keyAttr)
    print(length)
    for item in initialData:
        item[0] = keyAttr[0] + ": " + handleAge(item[0])
        item[1] = keyAttr[1] + ": " + handleGender(item[1])
        for j in range(2, length - 1):
            item[j] = keyAttr[j] + ": " + handleLevel(item[j])
        item[length - 1] = keyAttr[length - 1] + ": " + item[length - 1]
    # print("这里是重新命名后的" + initialData)
    processedData = {}
    for i in range(len(initialData)):
        processedData[i] = initialData[i]
    for item in processedData.values():
        print(item)
    return processedData


def handleAge(attr):
    tmp = ""
    if 7 < int(attr) <= 17:
        tmp = "少年"
    elif 17 < int(attr) <= 40:
        tmp = "中年"
    elif 40 < int(attr) <= 65:
        tmp = "老年"
    return tmp


def handleGender(attr):
    tmp = ""
    if attr == 1:
        tmp = "男"
    elif attr == 2:
        tmp = "女"
    return tmp


def handleLevel(attr):
    tmp = ""
    if 1 <= int(attr) <= 3:
        tmp = "轻度"
    elif 4 <= int(attr) <= 6:
        tmp = "中度"
    elif 7 <= int(attr) <= 10:
        tmp = "重度"
    return tmp


def xlsx_to_csv_pd():
    data_xls = pd.read_excel(
        '../处理后癌症病人数据.xlsx',
        index_col=0)  # 输入xlsx文件名
    data_xls.to_csv('../ProcessedData/patient.csv', encoding='utf-8')  # 输出csv文件名
    data_xls = pd.read_excel(
        '../processingData/cancerPatientDataSets.xlsx',
        index_col=0)  # 输入xlsx文件名
    data_xls.to_csv('../ProcessedData/patient2.csv', encoding='utf-8')  # 输出csv文件名


if __name__ == '__main__':
    pass
    # xlsx_to_csv_pd()
    # preprocessPatientDataMoreDetailedly(flag=1)
    # preprocessPatientDataHarshly()
