from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "new_project/index.html")

def vova(request):
    return HttpResponse("Hello, Vova!")

def greet(request, name):
    return HttpResponse(f"Hello, {name.capitalize()}!")