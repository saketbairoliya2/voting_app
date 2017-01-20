from django.conf.urls import url

from . import views

app_name = 'polls'
urlpatterns = [
	# Ex: /polls/
	url(r'^$', views.index, name='index'),
	# Ex: /polls/5/
	url(r'^(?P<question_id>[0-9]+)/$', views.details, name='details'),
	# Ex: /polls/5/results/
	url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
	# Ex: /polls/5/vote/
	url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]