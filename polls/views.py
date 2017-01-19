from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from django.template import loader

# Create your views here.

def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	template = loader.get_template('polls/index.html')
	context = {
		'latest_question_list': latest_question_list,
	}
	print(latest_question_list)
	return HttpResponse(template.render(context, request))

def details(request, question_id):
	return HttpResponse("The requested question here is %s" % question_id)

def results(request, question_id):
	response = "you are looking at the result of question {}"
	return HttpResponse("you are looking at the result of question {}" .format(question_id))

def vote(request, question_id):
	return HttpResponse("You're voting on question %s." % question_id)