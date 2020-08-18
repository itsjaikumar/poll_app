from django.shortcuts import render
from django.template import loader
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from django.http import JsonResponse

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list':latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, pk):
    question = Question.objects.get(id=pk)

    context = {
        'question':question
    }
    return render(request, 'polls/detail.html',context)

def results(request, pk):
    question = Question.objects.get(id=pk)
    context = {
        'question':question
    }
    return render(request, 'polls/results.html', context)

def vote(request, pk):
    question = Question.objects.get(id=pk)

    try :
        selected_choice = question.choice_set.get(id=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        context = {
            'question':question,
            'error_message':'You didnt selected any choice',
        }
        return render(request, 'polls/detail.html', context)
    else:
        selected_choice.votes +=1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))

def resultsData(request, obj):
    votedata = []

    question = Question.objects.get(id=obj)
    votes = question.choice_set.all()

    for i in votes:
        votedata.append({i.choice_text:i.votes})

    print(votedata)
    return JsonResponse(votedata, safe=False)

