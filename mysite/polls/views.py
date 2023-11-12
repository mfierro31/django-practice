from django.http import HttpResponse
from .models import Question
from .models import Choice
from django.shortcuts import render

def index(request):
    # The "-" before pub_date is a shortcut for saying "in descending order".  "pub_date" by itself would imply ascending order
    # [:5] is list slicing syntax that tells us take the first 5 results only (or, up to right before index of 5)
    latest_questions_list = Question.objects.order_by("-pub_date")[:5]
    context = {
        "latest_questions_list": latest_questions_list
    }
    return render(request, "polls/index.html", context)

def detail(request, question_id):
    q = Question.objects.get(pk=question_id)
    choices = Choice.objects.filter(question__id=question_id)
    print(choices)
    context = {
        "question": q,
        "choices": choices
    }
    return render(request, "polls/detail.html", context)

def results(request, question_id):
    return HttpResponse("You're looking at the results of question # %s." % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question # %s." % question_id)