from django.conf.urls import url
from lenongapp import views as v
urlpatterns =[
    url(r'register',v.index),
    url(r'ok/',v.useri,name='ok'),
    url(r'login/',v.login,name='login')
]