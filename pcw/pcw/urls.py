from django.contrib import admin
from django.urls import path, include
from . import home

urlpatterns = [
    path("", home, name="Home"),
    path('admin/', admin.site.urls),
    path("polls/", include("polls.urls"))
]
