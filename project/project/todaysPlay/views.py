from django.shortcuts import render, redirect
from django.template import loader
from django.contrib.auth.models import User
from django.contrib import auth
import random

# Create your views here.
def main(request):
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
    context = {
            'random': randomplay,
        }
    return render(request, 'main.html', context)
