from django.shortcuts import render
from django.template import loader

# Create your views here.

def main(request):
    context = None
    return render(request,'main.html',context)