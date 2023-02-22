from django.http import HttpResponse

def home(request):
    return HttpResponse("I am the root endpoint of the whole project")