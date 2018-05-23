from django.conf.urls import url
from lenongapp import views as v
urlpatterns =[
    url(r'register',v.index,name='register'),
    url(r'ok/',v.useri,name='ok'),
    url(r'login_handle/',v.login_handle),
    url(r'login/',v.login,name='login'),
    url(r'userinfo/',v.user_info,name='user_info'),
    url(r'site/',v.user_site,name='user_site'),
    url(r'site_handle/',v.site_handle,name='site_handle')
]