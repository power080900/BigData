from django.shortcuts import render, redirect
from django.http import HttpResponse
from todaysPlay.models import Subway
from django.contrib.auth.models import User
from todaysPlay.models import Cultureplace
from django.contrib import auth
import random

# Create your views here.
def main(request):
    context = None
    print(request.user.is_authenticated)
    print(request.user)
    j = random.randrange(1, 7)
    if request.user.is_authenticated:
        context = {
            'logineduser': request.user,
            'j': j,
            'link': ['미술관', '공연·전시장', '문화예술회관', '박물·기념관', '유적지', '문화원', '기타'],
            'link2': ['국악', '독주·독창회', '무용', '문화교양·강좌', '뮤지컬·오페라', '연극', '전시·미술', '콘서트', '클래식', '기타'],
        }
    else :
        context = {
            'j': j,
            'link': ['미술관', '공연·전시장', '문화예술회관', '박물·기념관', '유적지', '문화원', '기타'],
            'link2': ['국악', '독주·독창회', '무용', '문화교양·강좌', '뮤지컬·오페라', '연극', '전시·미술', '콘서트', '클래식', '기타'],
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
    placelist = Cultureplace.objects.filter(lineNumber__contains=line)
    print(placelist)
    xy = []
    for coordinate in placelist:
        xy.append({"name": coordinate.placeName, "lat": coordinate.lat, "lng": coordinate.lng})
    context = {
        "color": color,
        "hosun": hosunno,
        "hosun_1": hosunno_1,
        "hosun_2": hosunno_2,
        "hosun_3": hosunno_3,
        "xy": xy,
    }
    return render(request, 'googlemap.html', context)

def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        user = auth.authenticate(request, username=username, password=password)
        if user is not None :
            auth.login(request, user)
            return redirect("main:main")
        else :
            return render(request, 'loginpage.html', {'error': '사용자 아이디 또는 패스워드가 틀립니다.'})
    else :
        return render(request, 'loginpage.html')

def signInPage(request):
    res_data = None
    if request.method == 'POST':
        id = request.POST.get('id')
        password = request.POST.get('pw1')
        repassword = request.POST.get('pw2')
        res_data = {}
        if User.objects.filter(username=id):
            res_data['error'] = '이미 가입된 아이디입니다.'
        elif password != repassword:
            res_data['error'] = '비밀번호가 다릅니다.'
        else:
            user = User.objects.create_user(username=id, password=password)
            auth.login(request, user)
            return redirect("main:main")
    return render(request, 'signInPage.html', res_data)

def location1(request):
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
        '미술관': ['미술관1','미술관2'],
        '공연장': ['공연1', '공연장2', '공연장3'],
        '문화예술회관': ['세종문화회관', '예술의전당'],
        '박물관': ['박물관1', '박물관2','박물관4','박물관5',],
        '유적지': ['기타1', '기타2', '기타3', '기타4', ],
        '문화원': ['기타1', '기타2', '기타3', '기타4', ],
        '기타': ['기타1', '기타2', '기타3', '기타4', ],
    }
    return render(request, 'location1.html',context)

def location2(request):
    i = request.GET.get("pid")
    if i == "국악":
        title = "국악"
    elif i == "독주·독창회":
        title = "독주·독창회"
    elif i == "무용":
        title = "무용"
    elif i == "문화교양·강좌":
        title = "문화교양·강좌"
    elif i == "뮤지컬·오페라":
        title = "뮤지컬·오페라"
    elif i == "연극":
        title = "연극"
    elif i == "전시·미술":
        title = "전시·미술"
    elif i == "콘서트":
        title = "콘서트"
    elif i == "클래식":
        title = "클래식"
    elif i == "기타":
        title = "기타"
    context = {
        'title' : title,
        '국악': ['국악1','국악2'],
        '독창회': ['독주1', '독주2'],
        '무용': ['무용1', '무용2'],
        '문화교양강좌': ['강좌1', '강좌2'],
        '뮤지컬·오페라': ['뮤지컬1', '뮤지컬2'],
        '연극': ['연극1', '연극2'],
        '전시미술': ['전시1', '전시2'],
        '콘서트': ['콘서트1', '콘서트2'],
        '클래식': ['클래식1', '클래식2'],
        '기타': ['기타1', '기타2', '기타3', '기타4'],
    }
    return render(request, 'location2.html',context)

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

def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
    return redirect("main:main")