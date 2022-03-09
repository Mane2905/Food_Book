from django.urls import path
from . import views
urlpatterns=[
    path('',views.login,name='login'),
    path('register',views.register,name='register'),
    path('logout',views.logout,name='logout'),
<<<<<<< HEAD
=======
    path('index',views.index,name='index')
>>>>>>> dee17ae37cd145b15c0b16ca4915060bd0735f21
]