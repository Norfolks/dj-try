# from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import RequestContext, loader
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.views import generic

from .models import Question


class IndexView(generic.ListView):
	template_name = 'polls/templates/index.html'
	context_object_name = 'latest_questions_list'

	def get_queryset(self):
		"""Return the last five"""
		return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
	model = Question
	template_name = 'polls/templates/detail.html'

class ResultsView(generic.DetailView):
	model = Question
	template_name = 'polls/templates/results.html'


# def index(request):
# 	latest_questions_list = Question.objects.order_by('-pub_date')[:5]
# 	template = loader.get_template('polls/templates/index.html')
# 	context = RequestContext(request, {
# 		'latest_questions_list':latest_questions_list
# 		})
# 	return HttpResponse(template.render(context))

# def detail(request, question_id):
# 	question = get_object_or_404(Question, pk=question_id)
# 	return render(request, 'polls/templates/detail.html', {'question':question})

# def	 results(request, question_id):
# 	question = get_object_or_404(Question, pk=question_id)
# 	return render(request, 'polls/templates/results.html', {'question':question}) 

def vote(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		return render(request, 'polls/detail.html', {
			'question':question,
			'error_message':"You didn't slelect a choice.",
			})
	else:
		selected_choice.votes += 1
		selected_choice.save()
	return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))