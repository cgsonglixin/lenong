from django.conf.urls import url
from LeongGoodApp import views as v
urlpatterns =[
    url(r'detail/(\d+)/',v.detail,name='detail'),
    url(r'test/',v.test1),
    url(r'list/(?P<fkey>\d+)/(?P<pindex>\d+)',v.list,name='fruite'),
    url(r'index',v.index)
]