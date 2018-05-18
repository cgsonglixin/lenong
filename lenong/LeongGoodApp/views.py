from django.shortcuts import render
from LeongGoodApp import models
# Create your views here.
from django.http import HttpResponse
from django.core.paginator import *

def detail(request,details):
    a = models.GoodsInfo.book1.get(id=details)
    return render(request,'detail.html',{'a':a})

def test1(request):
    return render(request,'test1.html')

def list(request,fkey,pindex):
    con = models.GoodsInfo.book1.filter(g_type=fkey)
    con1 = models.GoodsInfo.book1.filter(g_type=fkey).order_by('-gclick')

    paginator = Paginator(con,1)
    con = paginator.page(int(pindex))
    return render(request, 'list.html', {'con': con,'fkey':fkey,'con1':con1[0:2]})

def index(request):
    title = models.Typeinfo.book.all()
    con = models.GoodsInfo.book1.filter(g_type=2)
    woter = models.GoodsInfo.book1.filter(g_type=3)
    context= {'con':con[0:3],'title':title,'woter':woter[0:3]}
    return  render(request,'index.html',context)
    # return HttpResponse (con.values())


def heheda(request):
    return render(request,'heheda.html')


