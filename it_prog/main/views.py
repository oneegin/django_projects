from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h4> План график команидровок </h4>')

def about(request):
    return HttpResponse('<h1> Автор Онегин С. Е. </h1>')
