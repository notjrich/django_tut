from django.shortcuts import render
#url(r'(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
#example url /polls/5/vote/
#url(r'(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),

#import HttpResponse
from django.http import HttpResponse
from django.template import loader

#import Models
from .models import Question

# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
            'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, question_id):
    return HttpResponse("You're looking a question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the resutls of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
