from django.http import JsonResponse
from django.shortcuts import render
from django.shortcuts import HttpResponse
import json
from DataMining.main import facade
# Create your views here.
from django.views.decorators.csrf import csrf_exempt


def respondDataToFront(preData):
    data = {
        'code': 200,
        'message': "获取成功",
        'data': preData
    }
    print("完成发送任务")
    return JsonResponse(data=data, safe=False)


lift = []
cosine = []
allConfidenced = []
kulczynski = []


@csrf_exempt
def process(request):
    # data = json.loads(request.body)
    # print(type(data))
    fileName = request.GET.get("fileName")
    support = request.GET.get("support")
    confident = request.GET.get("confident")
    alg = request.GET.get("alg")
    preData = {}

    tabledata, liftList, cosineList, allConfidencedList, kulczynskiList = facade(alg, float(support), float(confident), fileName)

    print("这里是process")
    print(type(liftList))
    global lift, cosine, allConfidenced, kulczynski
    lift.extend(liftList)
    print(lift)
    cosine.extend(cosineList)
    allConfidenced.extend(allConfidencedList)
    kulczynski.extend(kulczynskiList)
    preData['tabledata'] = tabledata
    # preData['freq'] = freq
    return HttpResponse(respondDataToFront(preData))


def showResult(request):
    preData = {}
    # global lift
    lst = []
    print(lift)
    for i in range(len(lift)):
        dic = {}
        dic['lift'] = lift[i].assessmentOfQuantity
        dic['cosine'] = cosine[i].assessmentOfQuantity
        dic['allConfidenced'] = allConfidenced[i].assessmentOfQuantity
        dic['Kulczynski'] = kulczynski[i].assessmentOfQuantity
        dic['frontItemSets'] = lift[i].frontItemSets
        dic['latterItemSets'] = lift[i].latterItemSets
        # dic['']
        # print(item.assessmentOfQuantity, "  ", item.frontItemSets, "--->", item.latterItemSets)
        lst.append(dic)
    print("这里是showResult")
    # for item in lst:
    #     print(item)
    preData['patternAccess'] = lst

    return HttpResponse(respondDataToFront(preData))


# def next
# facade("Apriori", 0.02, 0.7, ' fileName')