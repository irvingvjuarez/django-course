from django.shortcuts import render, get_object_or_404, redirect
# from django.http import HttpResponse, HttpResponseRedirect

from .models import Question
# Create your views here.

def index(request):
    latest_question_list = Question.objects.all()
    return render(request, "polls/index.html", {
        "latest_question_list": latest_question_list
    })

def detail(request, question_id):
    question = get_object_or_404(Question, id=question_id)

    return render(request, "polls/detail.html", {
        "id": question.id,
        "paramId": question_id,
        "content": question.content,
        "choices": question.choice_set.all()
    })

def results(request, question_id):
    question = Question.objects.get(id=question_id)
    options = question.choice_set.all()
    votes = [{"content": opt.content, "votes": opt.votes} for opt in options ]

    return render(request, "polls/results.html", {
        "id": question.id,
        "paramId": question_id,
        "content": question.content,
        "votes": votes
    })

def vote(request, question_id):
    question = get_object_or_404(Question, id=question_id)

    try:
        chosenChoice = question.choice_set.get(id=request.POST["choice"])
    except:
        return render(request, "polls/detail.html", {
            "error_message": "An error has ocurred"
        })
    else:
        chosenChoice.votes += 1
        chosenChoice.save()

        return redirect("polls:results", question.id)