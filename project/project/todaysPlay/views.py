from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User
from django.contrib import auth
import random

# Create your views here.
def main(request):
    return render(request, 'main.html')

def randomslot(request):
    randint = random.randrange(1, 16)
    if randint == 1:
        subwayNo = '1호선'
    elif randint == 2:
        subwayNo = '2호선'
    elif randint == 3:
        subwayNo = '3호선'
    elif randint == 4:
        subwayNo = '4호선'
    elif randint == 5:
        subwayNo = '5호선'
    elif randint == 6:
        subwayNo = '6호선'
    elif randint == 7:
        subwayNo = '7호선'
    elif randint == 8:
        subwayNo = '8호선'
    elif randint == 9:
        subwayNo = '9호선'
    elif randint == 10:
        subwayNo = '분당선'
    elif randint == 11:
        subwayNo = '신분당선'
    elif randint == 12:
        subwayNo = '중앙선'
    elif randint == 13:
        subwayNo = '경춘선'
    elif randint == 14:
        subwayNo = '경의선'
    elif randint == 15:
        subwayNo = '공항철도'
    return HttpResponse(subwayNo)

def map(request):
    return render(request, 'googlemap.html')

def loginPage(request):
    return render(request, 'loginPage.html')