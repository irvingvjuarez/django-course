from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Index of the Polls app")

def detail(request, question_id):
    return HttpResponse(f"You are in the question #{question_id}")

def results(request, question_id):
    return HttpResponse(f"Results page of the question #{question_id}")

def vote(request, question_id):
    return HttpResponse(f"Here you should be able to vote in the question #{question_id}")