from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name='index'),
    path('<int:restaurant_id>',views.restaurant,name='restaurant'),
    path('custorder',views.custorder,name='custorder'),
    path('cart',views.cart,name='cart'),
    path('viewcart',views.viewcart,name='viewcart'),
    path('delcart',views.delcart,name = 'delcart'),
    path('last_order',views.last_order,name = 'last_order')]