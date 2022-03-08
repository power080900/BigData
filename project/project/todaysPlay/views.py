from django.shortcuts import render
from django.http import HttpResponse
from todaysPlay.models import Subway
import random

# Create your views here.
def main(request):
    j = random.randrange(1,7)
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
        subwayNo = '수인분당선'
    elif randint == 11:
        subwayNo = '신분당선'
    elif randint == 12:
        subwayNo = '경의선'
    elif randint == 13:
        subwayNo = '경춘선'
    elif randint == 14:
        subwayNo = '우이신설경전철'
    elif randint == 15:
        subwayNo = '공항철도'
    return HttpResponse(subwayNo)

def map(request):
    line = request.GET.get("line")
    if "1호선" in line:
        color = "#000099"
    elif "2호선" in line:
        color = "#008000"
    elif "3호선" in line:
        color = "#ff6600"
    elif "4호선" in line:
        color = "#0099ff"
    elif "5호선" in line:
        color = "#9900cc"
    elif "6호선" in line:
        color = "#993333"
    elif "7호선" in line:
        color = "#666633"
    elif "8호선" in line:
        color = "#e6005c"
    elif "9호선" in line:
        color = "#cc9900"
    elif "수인분당선" in line:
        color = "#ffcc00"
    elif "신분당선" in line:
        color = "#cc0000"
    elif "경의선" in line:
        color = "#00cc99"
    elif "경춘선" in line:
        color = "#00cc66"
    elif "우이신설경전철" in line:
        color = "#993333"
    else:
        color = "#33ccff"
    subwaylist = Subway.objects.filter(hosun__contains=line)
    hosunno, hosunno_1, hosunno_2, hosunno_3  = [], [], [], []
    for data in subwaylist:
        if line+"_1" in data.hosun:
            hosunno_1.append({"lat": data.lat, "lng": data.lng})
        elif line+"_2" in data.hosun:
            hosunno_2.append({"lat": data.lat, "lng": data.lng})
        elif line+"_3" in data.hosun:
            hosunno_3.append({"lat": data.lat, "lng": data.lng})
        else:
            hosunno.append({"lat": data.lat, "lng": data.lng})
    context = {
        "color": color,
        "hosun": hosunno,
        "hosun_1": hosunno_1,
        "hosun_2": hosunno_2,
        "hosun_3": hosunno_3,
    }
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
        'place1' :['경복궁','창경궁'],
        'place2' : ['몽촌토성', '정릉', '선정릉'],
        'place3': ['세종문화회관', '예술의전당'],
        'place4': ['박물관1', '박물관2','박물관4','박물관5',],
        'place5': ['기타1', '기타2', '기타3', '기타4', ],
    }
    return render(request, 'location.html',context)

def info(request):
    title = request.GET.get("pid")
    contents = "연습용 내용 넣기"
    context = {
        'info' : {
            'title' : title,
            'contents' : contents,
        },
    }
    return render(request, 'info.html', context)
