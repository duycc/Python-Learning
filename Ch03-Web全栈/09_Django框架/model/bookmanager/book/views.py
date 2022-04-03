from django.http import HttpResponse
from django.shortcuts import render
from book.models import BookInfo, PeopleInfo
from django.db.models import F, Q

# Create your views here.


def index(request):
    books = BookInfo.objects.all()

    context = {'books': books}
    return HttpResponse('index')


# 1. 增加数据
# save()
book = BookInfo(
    name='Python',
    pub_date='2022-04-03',
)
book.save()

# create
BookInfo.objects.create(
    name='Cpp',
    pub_date='2022-04-03',
)

# 2. 修改
# save
book = BookInfo.objects.get(id=5)
book.readcount = 22
book.save()

# update
BookInfo.objects.filter(name='Cpp').update(readcount=33)

# 3. 删除
book = BookInfo.objects.get(name='Python')
book.delete()

BookInfo.objects.filter(name='Cpp').delete()
