from django.shortcuts import render
from .models import book_title
# Create your views here.

def index(request):
    book_list = book_title.objects.all()
    context = {'book_list':book_list}
    return render(request, 'books/index.html',context)