from .models import Question
from django.shortcuts import get_object_or_404, render

def index(request):
    # The "-" before pub_date is a shortcut for saying "in descending order".  "pub_date" by itself would imply ascending order
    # [:5] is list slicing syntax that tells us take the first 5 results only (or, up to right before index of 5)
    latest_questions_list = Question.objects.order_by("-pub_date")[:5]
    context = {
        "latest_questions_list": latest_questions_list
    }
    return render(request, "polls/index.html", context)

def detail(request, question_id):
    q = get_object_or_404(Question, pk=question_id)
    context = {
        "question": q
    }
    return render(request, "polls/detail.html", context)

def results(request, question_id):
    q = get_object_or_404(Question, pk=question_id)
    context = {
        "question": q
    }
    return render(request, "polls/results.html", context)

def vote(request, question_id):
    q = get_object_or_404(Question, pk=question_id)
    context = {
        "question": q
    }
    return render(request, "polls/vote.html", context)