from django.shortcuts import render, HttpResponse

def index(request):
    return render(request, 'index.html')

def hello(request, name):
    greeting = f'hello, {name}'
    return render(request, 'hello.html', {'greeting': greeting}) # render(처음엔 무조건 request, 어디서?, 할 일
