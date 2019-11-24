from django.shortcuts import render
from django.template import loader
from polls.models import Choice,Question,User
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

def index(request):
    latest_question_list = Question.objects.all().order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}

    if request.session.get('loginuser'):
        context['loginuser'] = request.session.get('loginuser')

    return render(request,'polls/index.html',context)

def loginview (request):
    return render(request, 'polls/login.html')

def loginprocess (request):
    try:
        user = User.objects.get(user_id=request.POST['userid'],
                                user_password=request.POST['userpassword'])
        print(user.user_name, request.POST['userid'],request.POST['userpassword'])

        request.session['loginuser'] = user.user_name

        if request.POST["idsave"] :
            print(request.POST["idsave"])

            content = loader.render_to_string('polls.main.html', None, request, None)
            response = HttpResponse(content,None,None)
            response.set_cookie('userid',request.POST['userid'], 60*60*24)
            return response

    except (KeyError, User.DoesNotExist):
        return render(request, 'polls/main.html', {
            'error_message':"로그인 실패",
        })
    return render(request, 'polls/main.html', {'loginuser':user.user_name})
# def test1(request):
#     latest_question_list = Question.objects.all().order_by('-pub_date')[:5]
#     context = {'latest_question_list': latest_question_list}
#     return render(request,'polls/test1.html',context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk =question_id)
    return render(request, 'polls/detail.html',{'question':question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request,'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice",

        })
    else:
        selected_choice.votes += 1
        selected_choice.save()

        return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))

def results(request, question_id):
    question = get_object_or_404(Question,pk=question_id)
    return render(request,'polls/results.html',{'question':question})



