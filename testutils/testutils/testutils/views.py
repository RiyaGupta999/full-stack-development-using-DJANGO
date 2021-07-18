# Vishal has created this file-Harry
from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    # return HttpResponse("<h1>Home</h1>")
    return render(request, 'index.html')

def removepunc(request):
    print(request.GET.get('text','default'))
    return HttpResponse("remove punc ")

def capfirst(request):
    return HttpResponse("capital")

def newlineremove(request):
    return HttpResponse("newline")

def spaceremove(request):
    return HttpResponse("space")

def charcount(request):
    return HttpResponse("char")


