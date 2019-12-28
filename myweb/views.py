from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,redirect
# Create your views here.

def home(request):

    return render(request,'homepage.html')

def proj(request):

    return render(request,'proj.html')

def pics(request):
    return render(request,'pics.html')



def home2(request):
    return render(request,'homepage.html')