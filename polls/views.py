from django.shortcuts import render
from django.http import Http404
#url(r'(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
#example url /polls/5/vote/
#url(r'(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),

#import Models
from .models import Question

# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list,}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'quesiton': question})

def results(request, question_id):
    response = "You're looking at the resutls of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
