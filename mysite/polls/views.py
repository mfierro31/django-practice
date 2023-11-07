from django.http import HttpResponse
from .models import Question


def index(request):
    # The "-" before pub_date is a shortcut for saying "in descending order".  "pub_date" by itself would imply ascending order
    # [:5] is list slicing syntax that tells us take the first 5 results only (or, up to right before index of 5)
    latest_questions_list = Question.objects.order_by("-pub_date")[:5]
    output = ", ".join([q.question_text for q in latest_questions_list])
    return HttpResponse(output)

def detail(request, question_id):
    return HttpResponse("You're looking a question # %s." % question_id)

def results(request, question_id):
    return HttpResponse("You're looking at the results of question # %s." % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question # %s." % question_id)