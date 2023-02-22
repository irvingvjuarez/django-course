from django.shortcuts import render
from django.http import HttpResponse

from .models import Question
# Create your views here.

def index(request):
    latest_question_list = Question.objects.all()
    return render(request, "polls/index.html", {
        "latest_question_list": latest_question_list
    })

def detail(request, question_id):
    return HttpResponse(f"You are in the question #{question_id}")

def results(request, question_id):
    return HttpResponse(f"Results page of the question #{question_id}")

def vote(request, question_id):
    return HttpResponse(f"Here you should be able to vote in the question #{question_id}")