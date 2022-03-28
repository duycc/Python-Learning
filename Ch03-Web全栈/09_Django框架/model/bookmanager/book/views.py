from os import lseek
from django.http import HttpResponse
from django.shortcuts import render
from book.models import BookInfo

# Create your views here.


def index(request):
    books = BookInfo.objects.all()

    context = {
        'books': books
    }
    return HttpResponse('index')
