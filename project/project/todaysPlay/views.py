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
    j = random.randrange(1,7)
    context = {
        'j' : j,
        'link' : ['미술관','공연·전시장','문화예술회관','박물·기념관','유적지','문화원','기타'],
        'link2': ['국악','독주·독창회','무용','문화교양·강좌','뮤지컬·오페라','연극', '전시·미술', '콘서트', '클래식', '기타'],
    }

    return render(request, 'main.html', context)

def randomslot(request):
    randint = random.randrange(1, 16)
    if randint == 1:
        subwayNo = '01호선'
    elif randint == 2:
        subwayNo = '02호선'
    elif randint == 3:
        subwayNo = '03호선'
    elif randint == 4:
        subwayNo = '04호선'
    elif randint == 5:
        subwayNo = '05호선'
    elif randint == 6:
        subwayNo = '06호선'
    elif randint == 7:
        subwayNo = '07호선'
    elif randint == 8:
        subwayNo = '08호선'
    elif randint == 9:
        subwayNo = '09호선'
    elif randint == 10:
        subwayNo = '분당선'
    elif randint == 11:
        subwayNo = '신분당선'
    elif randint == 12:
        subwayNo = '경의선'
    elif randint == 13:
        subwayNo = '경춘선'
    elif randint == 14:
        subwayNo = '경의선'
    elif randint == 15:
        subwayNo = '공항철도'
    return HttpResponse(subwayNo)

def map(request):
    line = request.GET.get("line")
    print(line)
    subwaylist = Subway.objects.filter(hosun__exact=line)
    hosunno = []
    print(subwaylist)
    for data in subwaylist:
        hosunno.append({"lat": data.lat, "lng": data.lng})
    context = {
        "hosun": hosunno,
    }
    return render(request, 'googlemap.html', context)

def loginPage(request):
    return render(request, 'loginPage.html')

def signInPage(request):
    return render(request, 'signInPage.html')

def location(request):
    i = request.GET.get("pid")
    if i == "미술관":
        title = "미술관"
    elif i == "공연·전시장":
        title = "공연·전시장"
    elif i == "문화예술회관":
        title = "문화예술회관"
    elif i == "박물·기념관":
        title = "박물·기념관"
    elif i == "유적지":
        title = "유적지"
    elif i == "문화원":
        title = "문화원"
    elif i == "기타":
        title = "기타"
    context = {
        'title' : title,
        'place1': ['미술관1','미술관2'],
        'place2': ['공연1', '공연장2', '공연장3'],
        'place3': ['세종문화회관', '예술의전당'],
        'place4': ['박물관1', '박물관2','박물관4','박물관5',],
        'place5': ['기타1', '기타2', '기타3', '기타4', ],
        'place6': ['기타1', '기타2', '기타3', '기타4', ],
        'place7': ['기타1', '기타2', '기타3', '기타4', ],
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
