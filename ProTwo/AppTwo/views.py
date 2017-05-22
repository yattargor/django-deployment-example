from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse('<em>My Second App del cazzo</em>')

def help(request):
    two_dict = {'help_me':"I inserted this help notations!"}
    return render(request,'AppTwo/help.html', context = two_dict)
