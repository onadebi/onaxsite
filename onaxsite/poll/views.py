from django.shortcuts import render, get_object_or_404;
from .models import Question;
from django.http import HttpResponse, Http404, HttpRequest;

# Create your views here.
def index(request: HttpRequest):
    # http://127.0.0.1:8000/home/?name=onadebi
    latest_questions = Question.objects.order_by("-pub_date")[:5];
    # output =",".join([q.question_text for q in latest_questions]);
    context = {"latest_question_list": latest_questions};
    return render(request, "poll/index.html", context)

def detail(request, question_id: int):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    #region Alternative to the above
    question = get_object_or_404(Question, pk=question_id)
    #endregion
    return render(request, "poll/detail.html", {"question": question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)