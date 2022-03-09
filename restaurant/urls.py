from django.urls import path
from . import views
urlpatterns=[
    path('',views.index_rest,name='restaddress'),
    path('menu',views.menu,name='restindex'),
    path('order',views.order,name='order')]