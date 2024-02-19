from django.http import HttpResponse
from django.shortcuts import render
def fun1(request):
    return HttpResponse("welcome")
