import pandas as pd
import csv


def preprocessInsuranceData():
    sourcedata = pd.read_csv(r"../processingData/insurance.csv", encoding="GBK")
    # print(sourcedata)
    sourcedata = sourcedata.values
    # print(head)
    length = len(sourcedata)
    print(length)
    processdata = []
    for item in sourcedata:
        temp = []
        if item[0] <= 15:
            temp.append('child')
        elif 15 < item[0] <= 25:
            temp.append('teenager')
        elif 25 < item[0] <= 60:
            temp.append('middle-age')
        else:
            temp.append('old')
        temp.append(item[1])
        if item[2] < 18.0:
            temp.append('thin')
        elif 24.0 >= item[2] >= 18.0:
            temp.append('healthy')
        else:
            temp.append('fat')
        if item[3] > 0:
            temp.append('have child')
        else:
            temp.append('no child')
        if item[4] == 'yes':
            temp.append('smoke')
        else:
            temp.append('no smoke')
        temp.append(item[5])
        if item[6] < 5000.00:
            temp.append('low-input')
        elif 5000.00 <= item[6] < 10000.00:
            temp.append('middle-input')
        else:
            temp.append('high-input')
        processdata.append(temp)
    print(processdata)
    with open('../ProcessedData/process_insurance.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for row in processdata:
            writer.writerow(row)


def insurenceDataProcessing(flag=1):
    initialData = pd.read_csv(
        "../ProcessedData/process_insurance.csv",
        encoding='utf-8',
        sep=',')
    initialData = initialData.values
    keyAttr = ['age', 'sex', 'bmi', 'children', 'smoker', 'region', 'charges']
    # print(initialData)
    length = len(keyAttr)
    pData = []
    for item in initialData:
        tmp = []
        for i in range(length):
            tmp.append(item[i])
        pData.append(tmp)
        # print(tmp, '\n')
    processedData = {}
    for i in range(len(pData)):
        processedData[i] = pData[i]
    return processedData
