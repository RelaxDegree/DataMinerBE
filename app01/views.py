from django.shortcuts import render
from django.shortcuts import HttpResponse


# Create your views here.
from django.views.decorators.csrf import csrf_exempt


# @csrf_exempt
def process(request):
    return HttpResponse("welcome")
