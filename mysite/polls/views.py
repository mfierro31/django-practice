from .models import Question, Choice
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse

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
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))