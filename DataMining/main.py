import util_m
from DataMining import apriori
from DataMining import fp_growth
from DataMining.TheRomanceOfThreeKingdomsDataProcess import TheRomanceOfThreeKingdomsDataPreprocessing
from DataMining.theNationalCongressDataPreprocessing import TheNationalCongressDataPreprocessing
from sys import stdin
from DataMining.countWordFrequency import CountWordFrequency
from DataMining.insuranceDataProcessing import insurenceDataProcessing
from DataMining.patientDataProcessing import preprocessPatientDataHarshly, preprocessPatientDataMoreDetailedly
from DataMining.patternAssess import PatternAssess
import pandas as pd
from DataMining.shoppingBasketDataProcess import preprocessShoppingtData2

def facade(ftype, support, confidence, fileName):
    # data = patientDataPreprocessing()
    theNationalCongressDataPreprocessing = TheNationalCongressDataPreprocessing()
    threeKingdomsDataProcess = TheRomanceOfThreeKingdomsDataPreprocessing()
    cwf = CountWordFrequency()
    print("请输入\n"
          "选择频繁模式挖掘算法（1：Apriori  2：fp-growth）\n"
          "支持度 置信度(0,1)\n"
          "以空格分隔 如：“2 0.05 0.05 "
          "输入#退出")

    # data = preprocessPatientDataHarshly()
    # data = preprocessPatientDataMoreDetailedly()
    # data = insurenceDataProcessing()
    # data = threeKingdomsDataProcess.dataPreprocessing()
    data = theNationalCongressDataPreprocessing.dataPreprocessing()
    # data = preprocessShoppingtData2()
    # print('这里时预处理后的数据', data)
    if ftype == "Apriori":
        apr = apriori.Apriori(datas=data, support=support, confidence=confidence)
        # print(apr.freq_set)
        print(util_m.relate_rules2str(apr.rel_rules))
        pa = PatternAssess(data, apr.rel_rules)
        pa.calculateLiftAndCosine()
        pa.calculateAllConfidenced()
        pa.calculateKulczynski()
    elif ftype == 'FP-growth':
        # print(data)
        fp = fp_growth.FPGrowth(datas=data, support=support, confidence=confidence)
        # print("频繁模式树为：")
        # fp.fp_tree_root_point.print()
        # print("频繁项集", fp.freq_set)
        # print("未格式化的关联规则",fp.relate_rule)
        print(util_m.relate_rules2str(fp.relate_rule))
        print("下面是模式评估相关量：**********************************************************************************")
        pa = PatternAssess(data, fp.relate_rule)
        liftRPList, cosineRPList = pa.calculateLiftAndCosine()
        pa.calculateAllConfidenced()
        pa.calculateKulczynski()
        # print()
        lenth = len(data)
        data['size'] = lenth
        return data, fp.freq_set, liftRPList, cosineRPList
'''
对于病人数据集结果不错的参数有 : 2 0.3 0.7 ;
购物篮1: 2 0.02 0.025
购物篮2 groceries: 

'''
