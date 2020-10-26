from django.shortcuts import render, HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("Landing Page")


def signin(request):
    pass


def signout(request):
    pass


def dashboard(request):
    pass
