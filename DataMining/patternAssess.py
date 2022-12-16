# -*- coding:utf-8 -*-
"""
作者：hp
日期：2022年 11月01日
"""
import math
import copy
from operator import attrgetter


class RelationPrinciple:
    def __init__(self):
        self.assessmentOfQuantity = 0.0
        self.frontItemSets = []
        self.latterItemSets = []

    def setValue(self, a, f, l):
        self.assessmentOfQuantity = a
        self.frontItemSets = list(f)
        self.latterItemSets = list(l)
        return self

    def __lt__(self, other):
        return self.assessmentOfQuantity > other.assessmentOfQuantity

    def __repr__(self):
        return 'RelationPrinciple({})'.format(self.assessmentOfQuantity)


class PatternAssess:

    def __init__(self, processedData: dict, relationPrincipleList: dict):
        self.offset = 30
        self.data = processedData
        self.relationPrincipleList = relationPrincipleList
        self.PAList = []
        self.PBList = []
        self.PABList = []
        self.recordNum = 0

    def calculateLiftAndCosine(self):
        # print("这里在计算提升度", self.data)
        # print("这里在计算提升度,这是关联规则", self.relationPrincipleList)
        liftRPList = []
        cosineRPList = []
        lift = []
        cosine = []
        recordNum = float(len(self.data))
        self.recordNum = recordNum
        for key, value in self.relationPrincipleList.items():
            PAB = 0.0
            PA = 0.0
            PB = 0.0
            for record in self.data.values():
                itemA = key
                itemB = value
                flag1 = 1  # 为1表示该项集在该记录中出现
                flag2 = 1
                for i in itemA:
                    if i not in record:
                        flag1 = 0

                for j in itemB:
                    if j not in record:
                        flag2 = 0
                if flag1: PA += 1
                if flag2: PB += 1
                if flag1 and flag2: PAB += 1
            self.PAList.append(PA)
            self.PBList.append(PB)
            self.PABList.append(PAB)
            templift = PAB * recordNum / (PA * PB)
            tempcosine = PAB / (math.sqrt(PA * PB))
            liftRPList.append((RelationPrinciple().setValue(templift, key, value)))
            cosineRPList.append(RelationPrinciple().setValue(tempcosine, key, value))
            # lift.append(templift)
            # cosine.append(tempcosine)
        # print("Lift：", lift)  # >1，后越大二者正关联性越强
        # print("IS:", cosine)  # 越接近1二者关联性越强
        # sorted(liftRPList, key=attrgetter("assessmentOfQuantity"))
        print("提升度： \n")
        liftRPList.sort()
        for item in liftRPList[:self.offset]:
            print(item.assessmentOfQuantity, "  ", item.frontItemSets, "--->", item.latterItemSets)
        print(
            "*********************************************************************************************************")
        print("IS度量： \n")
        cosineRPList.sort()
        for item in cosineRPList[:self.offset]:
            print(item.assessmentOfQuantity, "  ", item.frontItemSets, "--->", item.latterItemSets)

    # 计算全置信度
    def calculateAllConfidenced(self):
        allConfidencedRPList = []
        k = 0
        for key, value in self.relationPrincipleList.items():
            allConfidencedRPList.append(
                RelationPrinciple().setValue(self.PABList[k] / (max(self.PAList[k], self.PBList[k])), key, value))
            k += 1
        allConfidencedRPList.sort()
        print("*******************************************************************************************************")
        print("全置信度： \n")
        for item in allConfidencedRPList[:self.offset]:
            print(item.assessmentOfQuantity, "  ", item.frontItemSets, "--->", item.latterItemSets)
        # print("all_confidenced:", allConfidenced)  # 越接近1二者关系越紧密

    # 计算库尔钦ski度量
    def calculateKulczynski(self):
        kulczynski = []
        # for i in range(len(self.PABList)):
        #     kulczynski.append(0.5 * (self.PABList[i] / self.PBList[i] + self.PABList[i] / self.PAList[i]))
        # print("kulczynski:", kulczynski)  # 越接近1二者关系越紧密
        k = 0
        for key, value in self.relationPrincipleList.items():
            kulczynski.append(RelationPrinciple().setValue(
                0.5 * (self.PABList[k] / self.PBList[k] + self.PABList[k] / self.PAList[k]), key, value))
            k += 1
        kulczynski.sort()
        print(
            "*********************************************************************************************************")
        print("库尔钦斯基度量： \n")
        for item in kulczynski[:self.offset]:
            print(item.assessmentOfQuantity, "  ", item.frontItemSets, "--->", item.latterItemSets)

# liftRPList = [RelationPrinciple(),RelationPrinciple(),RelationPrinciple()]
# liftRPList[0].setValue(50,"x1","x2")
# liftRPList[1].setValue(12,"x1","x2")
# liftRPList[2].setValue(43,"x1","x2")
# liftRPList.sort()
# print(liftRPList)
# dic={0: "a" ,1:"b"}
# print(dic[0])
