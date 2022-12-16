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


@csrf_exempt
def process(request):
    # data = json.loads(request.body)
    # print(type(data))
    fileName = request.GET.get("fileName")
    support = request.GET.get("support")
    confident = request.GET.get("confident")
    alg = request.GET.get("alg")
    print(fileName, float(support), float(confident), alg)
    preData = {}
    lst = ['11', '22', '33', '44']

    preData['node'] = 'welcome'
    preData['lst'] = lst
    facade(alg, float(support), float(confident), fileName)
    return HttpResponse(respondDataToFront(preData))

# def next
