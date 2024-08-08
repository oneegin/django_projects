from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h4> Любой текст </h4>')

def about(request):
    return HttpResponse('<h1> о нас </h1>')
