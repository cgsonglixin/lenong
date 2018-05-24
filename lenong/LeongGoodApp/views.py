
from django.shortcuts import render
from LeongGoodApp import models
# Create your views here.
from django.http import HttpResponse
from django.core.paginator import *
from django.db.models import Q

def detail(request,details):
    a = models.GoodsInfo.book1.get(id=details)
    return render(request,'detail.html',{'a':a})

def test1(request):
    return render(request,'test1.html')

def list(request,fkey,pindex):
    con = models.GoodsInfo.book1.filter(Q(g_type=fkey) & Q(g_User=29))
    con1 = models.GoodsInfo.book1.filter(Q(g_type=fkey) & Q(g_User=29)).order_by('-gclick')

    paginator = Paginator(con,3)
    con = paginator.page(int(pindex))
    return render(request, 'list.html', {'con': con,'fkey':fkey,'con1':con1[0:2]})

def index(request):
        uname = request.session.get('uname')
        # try:
        c = models.Userinfo.book2.get(utitle=uname)
        title = models.Typeinfo.book.all()
        con = models.GoodsInfo.book1.filter(Q(g_type=3) & Q(g_User=29))
        woter = models.GoodsInfo.book1.filter(Q(g_type=4) & Q(g_User=29))
        context = {'con': con[0:4], 'title': title, 'woter': woter[0:4]}
        return render(request, 'index.html', context)
    # except:
    #     a = models.Userinfo()
    #     a.utitle = uname
    #     a.save()
    #     title = models.Typeinfo.book.all()
    #     con = models.GoodsInfo.book1.filter(Q(g_type=1) & Q(g_User=29))
    #     woter = models.GoodsInfo.book1.filter(Q(g_type=2) & Q(g_User=29))
    #     context = {'con': con[0:4], 'title': title, 'woter': woter[0:4]}
    #     return render(request, 'index.html', context)

    # return HttpResponse (con.values())


def heheda(request,t_id):


    # int(t_id)
    # #获取session的值
    uname = request.session.get('uname')

    # #通过session来找到utitle相同的值
    gid = models.Userinfo.book2.get(utitle=uname)
    # gid = gid.id

    t_tt =models.GoodsInfo.book1.get(id=t_id)
    b = models.GoodsInfo()
    b.gtitle = t_tt.gtitle
    b.gpic  = t_tt.gpic
    b.gprice =  t_tt.gprice
    b.gjianjie = t_tt.gjianjie
    b.g_type = t_tt.g_type
    b.g_User = gid
    b.save()
    a = models.GoodsInfo.book1.filter(g_User=gid)
    return render(request,'cart.html',{'a':a,'uname':a})

def user_order(request):
    uname = request.session.get('uname')
    gid = models.Userinfo.book2.get(utitle=uname)
    gid = gid.id
    a = models.GoodsInfo.book1.filter(Q(g_User=gid) & Q(isDelete=1))
    b = models.GoodsInfo.book1.filter(Q(g_User=gid) & Q(isDelete=0))
    return render(request,'user_center_order.html',{'a':a,'b':b})

def cart(request):
    uname = request.session.get('uname')
    gid = models.Userinfo.book2.get(utitle=uname)
    a = models.GoodsInfo.book1.filter(g_User=gid)
    return render(request, 'cart.html', {'a': a, 'uname': a})