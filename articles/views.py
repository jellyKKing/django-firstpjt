from email import message
from django.shortcuts import render

def index(request):
    return render(request, 'articles/index.html')

def greeting(request):
    info = {'name' : '민지'}
    context = {'info' : info}
    return render(request, 'articles/greeting.html', context)

def throw(request):
    return render(request, 'articles/throw.html')

def catch(request):
    message = request.GET.get('message')
    context = {'message':message}
    return render(request, 'articles/catch.html', context)

def hello(request, name):
    context = {
        'name' : name
    }
    return render(request, 'articles/hello.html', context)