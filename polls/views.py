from curses.ascii import HT
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('Hello World Again!!!')
