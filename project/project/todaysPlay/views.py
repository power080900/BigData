from django.shortcuts import render, redirect
from django.template import loader
from django.contrib.auth.models import User
from django.contrib import auth
import random

# Create your views here.
def main(request):
    # context = None
    # print(request.user.is_authenticated)
    # print(request.user)
    randint = random.randrange(1,6)
    if randint == 1:
        randomplay = '맛있는거 먹자'
    elif randint == 2:
        randomplay = '재미있게 놀자'
    elif randint == 3:
        randomplay = '힐링 하자'
    elif randint == 4:
        randomplay = '운동 하자'
    elif randint == 5:
        randomplay = '구경 가자'
    # if request.user.is_authenticated:
    context = {
            # 'logineduser': request.user,
            'random': randomplay,
        }
    return render(request, 'main.html', context)

def register(request):
    res_data = None
    if request.method =='POST':
        useremail = request.POST.get('useremail')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        password = request.POST.get('password')
        re_password = request.POST.get('re-password')
        res_data = {}
        if User.objects.filter(username=useremail):
            res_data['error']='이미 가입된 아이디(이메일주소)입니다.'
        elif password != re_password:
            res_data['error']='비밀번호가 다릅니다.'
        else:
            user = User.objects.create_user(username = useremail,
                            first_name = firstname,
                            last_name = lastname,
                            password = password)
            auth.login(request, user)
            redirect("main.html")
    return render(request, 'register.html', res_data)  # 교육생들 수정!!!!


def login(request):
    if request.method == "POST":
        useremail = request.POST.get('useremail', None)
        password = request.POST.get('password', None)
        user = auth.authenticate(username=useremail, password=password)
        #print("***", user.date_joined)
        if user is not None :
            auth.login(request, user)
            return redirect("main:main")
        else :
            return render(request, 'login.html', {'error': '사용자 아이디 또는 패스워드가 틀립니다.'})
    else :
        return render(request, 'login.html')

def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
    return redirect("main:main")

def only_member(request) :
    context = None
    if request.user.is_authenticated:
        context = {'logineduser': request.user.last_name+request.user.first_name}
    return render(request, 'member.html', context)

