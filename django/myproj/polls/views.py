from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import loader

from .models import Question

# lodader를 이용한 방식(주석) / redner를 이용한 방식(shortcut)
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #template = loader.get_template('polls/index.html')
    context = {'latest_question_list':latest_question_list}
    #return HttpResponse(template.render(context, request))
    return render(request, 'polls/index.html', context)

def posts(request):
    print('ok')
    return render(request, 'main.html', {})

# Http404 모듈(주석) / get_object_or_404()(shortcut)
def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question':question})

def results(request, question_id):
    response = "You're looking at the results of questions %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)