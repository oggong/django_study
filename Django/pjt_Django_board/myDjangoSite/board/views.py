from django.shortcuts import render
from .forms import Loginform
from django.http import HttpResponseRedirect


from .models import User
from .models import Board


# Create your views here.

def login(request):
    form = Loginform()
    return render(request, "board/login.html", {'form': form})


def loginProcess(request):
    form = Loginform(request.POST)
    errormessage = ""

    if form.is_valid():
        login_id = form.cleaned_data["login_id"]
        login_pw = form.cleaned_data["login_pw"]
        print(login_id,login_pw)

        try:
            user = User.objects.get(pk=login_id,user_password=login_pw)
            print(user)
            if user :
                request.session["loginuser"] = user.user_name
                return HttpResponseRedirect("/board/boardList/1")
            else :
                errormessage = '1 로그인 실패. 다시 로그인 하세요'
                context = {"errormessage":errormessage}
                return render(request,"login.html",context)
        except(User.DoesNotExist):
            errormessage="2 로그인 실패. 다시 로그인 하세요"
            return render(request,"board/login.html",context)



def boardList(request, curr_page=1):
    if not request.session.get('loginuser'):
        return HttpResponseRedirect("/board/login")

    cntPerPage = 10
    endCnt = curr_page * cntPerPage
    startCnt = endCnt - cntPerPage
    print(startCnt,endCnt)

    totalCnt = Board.objects.count()
    tpn = int(totalCnt/cntPerPage + 1)
    totalPageCnt = []
    for i in range(1, tpn+1):
        totalPageCnt.append(i)

    board_list = Board.objects.all().order_by('-id')[startCnt:endCnt]
    context = {"board_list" : board_list, "totalPageCnt" : totalPageCnt, "curr_page":curr_page}
    return render(request, 'board/boardList.html',context)


def boardDetail(request, board_id=1):
    return render(request, 'board/boardList.html')
