from django.conf.urls import url
from LeongGoodApp import views as v
urlpatterns =[
    url(r'detail/(\d+)/',v.detail,name='detail'),
    url(r'test/',v.test1),
    url(r'list/(?P<fkey>\d+)/(?P<pindex>\d+)',v.list,name='fruite'),
    url(r'index',v.index,name='index'),
    url(r'hehehe/(\d+)',v.heheda,name='hehehe'),
    url(r'order/',v.user_order,name='user_order'),
    url(r'cart',v.cart,name='cart'),
    url(r'place_order',v.place_order,name='place_order')


]