from django.http import HttpResponse, HttpResponseRedirect
# from django.template import loader

from django.views import generic

from django.shortcuts import render, get_object_or_404

from .models import Question, Choice
from django.urls import reverse

from django.http import Http404

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published question."""
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DeleteView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DeleteView):
    model = Question
    template_name = "polls/results.html"

def vote(request, question_id):

    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request,'polls/detail.html',{'question':question, 'error_message': "You didn't select a choice",
                                                   })
    else:
        selected_choice.votes += 1
        selected_choice.save()
    # return HttpResponse("You're voting on question %s." % question_id)
        return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))
