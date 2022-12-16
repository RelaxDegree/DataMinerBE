# -*- coding:utf-8 -*-
"""
作者：hp
日期：2022年 10月31日
"""
import jieba
import re


class TheNationalCongressDataPreprocessing:
    def dataPreprocessing(self, flag=1):
        if flag == 1:
            data_set = 'E:\\pythonProject\\FreqSetDataMining\\eighttenNationalCongressOfCommunistPartyOfChina .txt'
            data_Write = 'E:\\pythonProject\\FreqSetDataMining\\res\PreprocessedEighttenNationalCongress'
        elif flag == 2:
            data_set = 'E:\\pythonProject\\FreqSetDataMining\\ninehttenNationalCongressOfCommunistPartyOfChina.txt'
            data_Write = 'E:\\pythonProject\\FreqSetDataMining\\res\PreprocessedNineteenNationalCongress'
        elif flag == 3:
            data_set = 'E:\\pythonProject\\FreqSetDataMining\\twentiethNationalCongressOfCommunistPartyOfChina.txt'
            data_Write = 'E:\\pythonProject\\FreqSetDataMining\\res\ProcessedTwentiethNationalCongress.txt'
        elif flag == 4:
            data_set = 'E:\\pythonProject\\FreqSetDataMining\\converge.txt'
            data_Write = 'E:\\pythonProject\\FreqSetDataMining\\res\PreprocessedConverge.txt'
        elif flag == 5:
            return self.dataPreprocessing()
        with open(data_set, 'r', encoding='UTF-8') as novelFile:
            novel = novelFile.read()
        novelList = re.split(r'([。？！；\n\u3000])', novel)
        # print(novelList[1:20])
        recordList = []
        print(novelList)

        # 针对每一句话进行分词
        for item in novelList:
            if item != '\n' and item != ' ' and item != '' and item != '。' and item != '\u3000':
                recordList.append(jieba.lcut(item))
        print(recordList)

        # 导入停词文件
        stopwords = [line.strip() for line in
                     open('E:\\pythonProject\\FreqSetDataMining\\stop.txt',
                          'r', encoding='UTF-8').readlines()]

        # print(wordList)

        # 每一句话去除停词
        temp = []
        result = []
        for record in recordList:
            for i in record:
                if i not in stopwords:
                    temp.append(i)
            result.append(temp)
            temp = []

        recordList = result
        print(recordList)
        lenRecordList = len(recordList)
        processedData = {}

        for i in range(lenRecordList):
            processedData[i] = recordList[i]
        # 下面输出预处理后的数据
        print(processedData)
        with open(data_Write, 'w', encoding='UTF-8') as processedDataFile:
            for key, value in processedData.items():
                processedDataFile.write(str(key))
                processedDataFile.write(': ')
                processedDataFile.write(str(value))
                processedDataFile.write(str('\n'))
        return processedData

# a = TheNationalCongressDataPreprocessing()
# a.dataPreprocessing(1)
