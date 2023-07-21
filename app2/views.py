from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first(request):
    return HttpResponse('<marquee><h1>Spider man into the mulitvers</h1></marquee>')

def second(request):
    return HttpResponse('<h1>The Spider MAN</h1>')