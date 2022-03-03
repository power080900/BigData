from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def main(request):
    context = {
        'link' : [1,2,3,4,5],
    }
    return render(request, 'main.html', context)

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

def signInPage(request):
    return render(request, 'signInPage.html')

def location(request):
    i = request.GET.get("pid")
    if i == "1":
        title = "고궁"
    elif i == "2":
        title = "유적지"
    elif i == "3":
        title = "극장/소극장"
    elif i == "4":
        title = "박물관/미술관"
    elif i == "5":
        title = "기타"
    context = {
        'title' : title,
    }
    return render(request, 'location.html',context)

def info(requset):
    return render(requset, 'info.html')