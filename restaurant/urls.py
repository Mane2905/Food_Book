from django.urls import path
from . import views
urlpatterns=[
    path('',views.index_rest,name='restaddress'),
    path('menu',views.menu,name='restindex'),
    path('order',views.order,name='order'),
    path('<int:order_no>',views.customer_order,name='customer_order'),
    path('deliver',views.deliver,name='deliver')]