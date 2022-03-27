from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.


def index(request):
    context = {'title': 'hello world'}
    # return HttpResponse('index')
    return render(request=request, template_name='Book/index.html', context=context)
