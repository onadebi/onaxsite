from django.shortcuts import render, get_object_or_404;
from django.db.models import F;
from django.urls import reverse;
from .models import Choice, Question;
from django.http import HttpResponse, Http404, HttpRequest, HttpResponseRedirect;

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


def results(request: HttpRequest, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "poll/results.html", {"question": question}, status=201)


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "poll/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("poll:results", args=(question.id,)))