from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
def fun1(request):
    return HttpResponse("hii...welcome to django")
def fun2(request,x):
    return HttpResponse("no of lecture taken"+x)
class admiralView(View):
    def get(self,request):
        return HttpResponse("inside fun3 admiral class is there")

def home(request):
    return render(request,'simple.html')