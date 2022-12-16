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


@csrf_exempt
def process(request):
    # data = json.loads(request.body)
    # print(type(data))
    fileName = request.GET.get("fileName")
    support = request.GET.get("support")
    confident = request.GET.get("confident")
    alg = request.GET.get("alg")
    preData = {}

    tabledata, freq, liftList, cosineList = facade(alg, float(support), float(confident), fileName)
    print(type(liftList))
    global lift
    lift.extend(liftList)
    preData['tabledata'] = tabledata
    # preData['freq'] = freq
    return HttpResponse(respondDataToFront(preData))


def showResult(request):
    preData = {}
    global lift
    lst = []
    for item in lift[:30]:
        dic = {}
        dic['assessmentOfQuantity'] = item.assessmentOfQuantity
        dic['frontItemSets'] = item.frontItemSets
        dic['latterItemSets'] = item.latterItemSets
        # print(item.assessmentOfQuantity, "  ", item.frontItemSets, "--->", item.latterItemSets)
        lst.append(dic)
    preData['lift'] = lst

    return HttpResponse(respondDataToFront(preData))

# def next
