from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homeview(request, *args, **kwargs):
    return render(request, "basic.html", {})

def index(request, *args, **kwargs):
    return render(request, "index.html", {})
    
def hmview(request, *args, **kwargs):
    return render(request, "baseone.html", {})