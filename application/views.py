from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import (HttpResponse, HttpResponseRedirect, render, reverse)

from .models import Travel, User

# Create your views here.


def index(request):
    context = {}
    if request.method == 'GET':
        if (request.user.is_authenticated):
            return render(request, "application/index.html", {
                "auth": True,
                "name": request.user.username.capitalize(),
            })
        else:
            return render(request, "application/index.html", {
                "auth": False,
            })

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("application:index"))
        else:
            messages.info(request, 'Username Or Password Incorrect')
            return render(request, 'application/index.html')
    return render(request, "application/index.html")


def signout(request):
    logout(request)
    return HttpResponseRedirect(reverse("application:index"))

@login_required(login_url='application:index')
def dashboard(request):
    trip = Travel.objects.filter(staff=request.user)
    return render(request, "application/dashboard.html", {
        "trips": trip
    })


def travelrequest(request):
    if request.method == "POST":
        value = request.POST
        try:
            new_travel_request = Travel(trip=value['trip'], traveldate=value['date'], staff=request.user)
            new_travel_request.save()
            return HttpResponseRedirect(reverse("application:dashboard"))
        except:
            messages.info(request, 'Incorrect Form Field')
            return HttpResponseRedirect(reverse("application:dashboard"))

