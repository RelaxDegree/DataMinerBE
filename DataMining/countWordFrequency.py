# -*- coding:utf-8 -*-
"""
作者：hp
日期：2022年 11月01日
"""
import jieba


class CountWordFrequency:
    def countWF(self, flag):
        if flag == 1:
            data_set = 'D:\homeworkInJLU\\firstEmesterOfJuniorYear\数据挖掘\\55200423王硕\FreqSetDataMining\\eighttenNationalCongressOfCommunistPartyOfChina .txt'
        elif flag == 2:
            data_set = 'D:\homeworkInJLU\\firstEmesterOfJuniorYear\数据挖掘\\55200423王硕\FreqSetDataMining\\ninehttenNationalCongressOfCommunistPartyOfChina.txt'
        elif flag == 3:
            data_set = 'D:\homeworkInJLU\\firstEmesterOfJuniorYear\数据挖掘\\55200423王硕\FreqSetDataMining\\twentiethNationalCongressOfCommunistPartyOfChina.txt'
        elif flag == 4:
            data_set = 'D:\homeworkInJLU\\firstEmesterOfJuniorYear\数据挖掘\\55200423王硕\FreqSetDataMining\\converge.txt'

        with open(data_set, 'r', encoding='UTF-8') as novelFile:
            novel = novelFile.read()
        stopwords = [line.strip() for line in
                     open('D:\homeworkInJLU\\firstEmesterOfJuniorYear\数据挖掘\\55200423王硕\FreqSetDataMining\\stop.txt', 'r', encoding='UTF-8').readlines()]
        temp = []
        wordList = list(jieba.lcut(novel))
        for i in wordList:
            if i not in stopwords:
                temp.append(i)
        wordList = temp
        # print(wordList)
        print('词汇总数：%d' % len(wordList))
        # print(novelList)
        wordDict = {}
        # print(novelList)
        # 统计出词频字典
        for word in wordList:
            if word not in stopwords:
                # 不统计字数为一的词
                if len(word) == 1:
                    continue
                else:
                    wordDict[word] = wordDict.get(word, 0) + 1

        # 对词频进行排序
        wordListSorted = list(wordDict.items())
        wordListSorted.sort(key=lambda e: e[1], reverse=True)
        # print(wordListSorted)
        # 打印前10词频
        topWordNum = 0
        recordNum = len(wordList)
        for topWordTup in wordListSorted[:10]:
            print(topWordTup[0], topWordTup[1] / recordNum)

# a = CountWordFrequency()
# a.countWF(1)
