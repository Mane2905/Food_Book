from django.shortcuts import render,redirect,reverse
from django.contrib import auth
from .models import Account
# Create your views here.


def register(request):
    if request.method=="POST":
        email= request.POST['email']
        password= request.POST['password']
        account_type=request.POST['account_type']
<<<<<<< HEAD
=======
        '''if account_type=="customer":
            username=account_type+email'''
>>>>>>> dee17ae37cd145b15c0b16ca4915060bd0735f21
        if Account.objects.filter(email = email).exists():
            return redirect('register')
        else:
            user = Account.objects.create_user( password = password,email=email,account_type=account_type)
            auth.login(request,user)
            if account_type=='customer':
                return redirect('/customer/')
            else:
                return redirect('/restaurant/')
    return render(request,'account/register.html')

def login(request):
    if request.method=="POST":
        email= request.POST['email']
        if Account.objects.filter(email = email).exists():
            username=Account.objects.filter(email=email)[0].email
            account_type=Account.objects.filter(email=email)[0].account_type
        password= request.POST['password']
        x=auth.authenticate(username=username,password=password)
        if x is not None:
            auth.login(request,x)
            if account_type[0]=='c':
                return redirect('/customer/')
            else:
                return redirect('/restaurant/')
        else:
            return redirect('login')
    return render(request,'account/login.html')


def logout():
    return redirect('login')
<<<<<<< HEAD
=======
def index(request):
    return render(request,'account\index.html') 
>>>>>>> dee17ae37cd145b15c0b16ca4915060bd0735f21
