
from django.urls import path
from . import views

app_name = "application"

urlpatterns = [
    path("", views.index, name="index"),
    path("signout/", views.signout, name="signout"),
    path("travelrequest/", views.travelrequest, name="travelrequest"),
    path("dashboard/", views.dashboard, name="dashboard"),

]
