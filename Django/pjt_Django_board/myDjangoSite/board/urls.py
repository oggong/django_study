from django.urls import path
from . import views

app_name = 'board'
urlpatterns=[
    path('login/',views.login, name='login'),
    path('loginProcess/',views.loginProcess,name='loginProcess'),
    path('',views.boardList,name='board'),
    path('boardList/<int:curr_page>', views.boardList, name='boardList'),
    path('boardDetail/<int:board_id>',views.boardDetail, name='boardDetail'),
]