from django.shortcuts import render,redirect
from django.http import HttpResponse
from lenongapp import models as lapp
from django.http import HttpResponseRedirect
from django.core.urlresolvers import  reverse
from LeongGoodApp import models as Laap

# Create your views here.
def index(request):
    return render(request,'register.html')


def useri(request):
    name = request.POST.get('user_name')
    pwd = request.POST.get('pwd')
    cpwd = request.POST.get('cpwd')
    email = request.POST.get('email')
    ok =  request.POST.get('allow')
    zhan = lapp.UserInfo.book.all()
    for i in zhan:
        if i.uname == name:
            return HttpResponse('已被注册')
        elif i.uemail == email:
            return HttpResponse('邮箱已被注册')

    if pwd == cpwd and ok == '123':
        a = lapp.UserInfo()
        a.uname = name
        a.upwd = pwd
        a.uemail = email
        a.save()
        return render(request, 'login.html')
    else:
        return HttpResponse('两次密码不一致')
    # try:
    #     a = models.UserInfo.book.get(uname=name)
    #     return HttpResponse('账号已存在')
    # except:
    #     if pwd == cpwd and ok == '123':
    #         a = models.UserInfo()
    #         a.uname = name
    #         a.upwd = pwd
    #         a.uemail = email
    #         a.save()
    #         return render(request, 'login.html')

def login_handle(request):
    username = request.POST.get('username')
    pwd = request.POST.get('pwd')
    str(username)
    str(pwd)
    try:
        a = lapp.UserInfo.book.get(uname=username)
        if a.upwd == pwd:
            request.session['uname'] = username
            uname = request.session.get('uname')
            b = Laap.Userinfo.book2.all()
            for b in b:
                if b.utitle == uname:
                    return redirect(reverse('goods:index'))
            a = Laap.Userinfo()
            a.utitle = uname
            a.save()
            return redirect(reverse('goods:index'))

        else:
            return HttpResponse('密码错误')

    except:
        return HttpResponse('没有用户')




def login(request):
    return render(request,'login.html')

def user_info(request):
    uname = request.session.get('uname')
    try:
        a = lapp.UserInfo.book.get(uname=uname)

        return  render(request,'user_center_info.html',{'a':a})
    except:
        return render(request,'user_center_info.html')

def user_site(request):
    uname = request.session.get('uname')
    try:
        a = lapp.UserInfo.book.get(uname=uname)

        return  render(request,'user_center_site.html',{'a':a})
    except:
        return render(request,'user_center_site.html')

def site_handle(request):
    name = request.POST.get('name')
    address = request.POST.get('address')
    post1 = request.POST.get('post1')
    shouji = request.POST.get('shouji')
    uname = request.session.get('uname')
    a = lapp.UserInfo.book.get(uname=uname)
    a.uaddress = address
    a.uzip_code = post1
    a.ureceive = name
    a.uphone = shouji
    a.save()
    return render(request, 'user_center_site.html', {'a': a})