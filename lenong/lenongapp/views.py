from django.shortcuts import render
from django.http import HttpResponse
from lenongapp import models
# Create your views here.
def index(request):
    return render(request,'register.html')


def useri(request):
    name = request.POST.get('user_name')
    pwd = request.POST.get('pwd')
    cpwd = request.POST.get('cpwd')
    email = request.POST.get('email')
    ok =  request.POST.get('allow')
    try:
        a = models.UserInfo.book.get(uname=name)
        return HttpResponse('账号已存在')
    except:
        if pwd == cpwd and ok == '123':
            a = models.UserInfo()
            a.uname = name
            a.upwd = pwd
            a.uemail = email
            a.save()
            return render(request, 'login.html')

def login(request):
    username = request.POST.get('username')
    pwd = request.POST.get('pwd')
    str(username)
    str(pwd)
    try:
        a = models.UserInfo.book.get(uname=username)
        if a.upwd == pwd:
            return render(request, 'index.html')
        else:
            return HttpResponse('密码错误')

    except:
        return HttpResponse('没有用户')







