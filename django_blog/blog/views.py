from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(Response):
    return HttpResponse('A new blog')