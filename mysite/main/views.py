from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homepage(reqest):
    return HttpResponse("TEST czy dziala")

