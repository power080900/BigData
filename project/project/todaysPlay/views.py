from django.shortcuts import render
from django.http import HttpResponse
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
import django
django.setup()
from todaysPlay.models import Subway
import random

# Create your views here.
def main(request):
    j =  random.randrange(1,7)
    context = {
        'j' : j,
        'link' : ['고궁','유적지','극장','박물관','기타'],
        'link2': ['연극', '체험', '전시회', '관람', '기타'],
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
    no1, no2, no3, no4, no5, no6, no7, no8, no9, no10 = [], [], [], [], [], [], [], [], [], []
    subwaylist = Subway.objects.all()
    for data in subwaylist:
        if "1호선" in data.hosun:
            no1.append({"lat": data.lat, "lng": data.lng})
        elif "2호선" in data.hosun:
            no2.append({"lat": data.lat, "lng": data.lng})
        elif "3호선" in data.hosun:
            no3.append({"lat": data.lat, "lng": data.lng})
        elif "4호선" in data.hosun:
            no4.append({"lat": data.lat, "lng": data.lng})
        elif "5호선" in data.hosun:
            no5.append({"lat": data.lat, "lng": data.lng})
        elif "6호선" in data.hosun:
            no6.append({"lat": data.lat, "lng": data.lng})
        elif "7호선" in data.hosun:
            no7.append({"lat": data.lat, "lng": data.lng})
        elif "8호선" in data.hosun:
            no8.append({"lat": data.lat, "lng": data.lng})
        elif "9호선" in data.hosun:
            no9.append({"lat": data.lat, "lng": data.lng})
        elif "경강선" in data.hosun:
            no10.append({"lat": data.lat, "lng": data.lng})
    context = {
        "no2": no2,
    }
    # stn = [data.stationName for data in subwaylist]
    # lat = [data.lat for data in subwaylist]
    # lng = [data.lng for data in subwaylist]
    # hosun = [data.hosun for data in subwaylist]
    # context = {
    #     "stationname": stn,
    #     "lat": lat,
    #     "lng": lng,
    #     "hosun": hosun,
    # }
    # return context
    return render(request, 'googlemap.html', context)

def loginPage(request):
    return render(request, 'loginPage.html')

def signInPage(request):
    return render(request, 'signInPage.html')

def location(request):
    i = request.GET.get("pid")
    if i == "고궁":
        title = "고궁"
    elif i == "유적지":
        title = "유적지"
    elif i == "극장":
        title = "극장/소극장"
    elif i == "박물관":
        title = "박물관/미술관"
    elif i == "기타":
        title = "기타"
    context = {
        'title' : title,
    }
    return render(request, 'location.html',context)

def info(requset):
    return render(requset, 'info.html')
