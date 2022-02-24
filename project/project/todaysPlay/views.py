from django.shortcuts import render
from django.template import loader
import random

# Create your views here.
def main(request):
    randint = random.randrange(1,6)
    if randint == 1:
        randomplay = '맛있는거 먹'
    elif randint == 2:
        randomplay = '재미있게 놀'
    elif randint == 3:
        randomplay = '힐링 하'
    elif randint == 4:
        randomplay = '운동 하'
    elif randint == 5:
        randomplay = '구경 가'
    context = {
        'random': randomplay,
    }
    return render(request,'main.html',context)