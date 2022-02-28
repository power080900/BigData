from django.shortcuts import render, redirect
from django.template import loader
from django.contrib.auth.models import User
from django.contrib import auth
import random

# Create your views here.
def main(request):
    randint = random.randrange(1,15)
    if randint == 1:
        randomplay = '1호선'
    elif randint == 2:
        randomplay = '2호선'
    elif randint == 3:
        randomplay = '3호선'
    elif randint == 4:
        randomplay = '4호선'
    elif randint == 5:
        randomplay = '5호선'
    elif randint == 6:
        randomplay = '6호선'
    elif randint == 7:
        randomplay = '7호선'
    elif randint == 8:
        randomplay = '8호선'
    elif randint == 9:
        randomplay = '9호선'
    elif randint == 10:
        randomplay = '분당선'
    elif randint == 11:
        randomplay = '신분당선'
    elif randint == 12:
        randomplay = '중앙선'
    elif randint == 13:
        randomplay = '경춘선'
    elif randint == 14:
        randomplay = '경의선'
    context = {
            'random': randomplay,
        }
    return render(request, 'main.html', context)
