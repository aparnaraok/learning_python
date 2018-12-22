from django.shortcuts import render
import datetime
# Create your views here.

from django.http import HttpResponse

def say_hello(request): #Pressing enter(GET) is the request
    return HttpResponse("Hello World...Welcome to the Django Framework")

def current_time_stamp(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>"%now
    return HttpResponse(html)
