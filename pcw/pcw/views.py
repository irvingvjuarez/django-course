from django.http import HttpResponse

def home(response):
    return HttpResponse("I am the root endpoint of the whole project")