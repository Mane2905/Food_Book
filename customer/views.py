from django.shortcuts import render,redirect
from restaurant.models import Restaurant,Menu,Order
from .models import Cart,Rec_Order

# Create your views here.
def index(request):
    rest = Restaurant.objects.order_by('-uid')
    context={
        'cont':rest,
    }
    return render(request,'customer/index.html',context)

def restaurant(request,restaurant_id):
    menu=Menu.objects.order_by('-price').filter(uid=restaurant_id)
    cust=request.user.email
    context={
        'content':menu,
        'cust':cust
    }
    return render(request,'customer/restaurant.html',context)
def custorder(request):
    if request.method=="POST":
        status=request.POST['status']
        uid = request.POST['uid']
        cust_id = request.POST['customid']
        item = request.POST['item']
        price= request.POST['price']
        d=Rec_Order.objects.filter(cust_id=cust_id)
        d.delete()
        b = Restaurant.objects.filter(uid = uid)[0]
        p = Rec_Order(uid=uid,name=b.hotel,order_no=1,cust_id=cust_id,item=item,price=price)
        p.save()
        if Order.objects.filter(uid=uid).exists():
            a=Order.objects.filter(uid=uid).order_by('-order_no')[0]
            c = Order(uid=uid,order_no=((a.order_no)+1),cust_id=cust_id,item=item,price=price,status=status)
            c.save()
        else: 
            c = Order(uid=uid,order_no=1,cust_id=cust_id,item=item,price=price,status=status)
            c.save()
    return redirect('last_order')

def cart(request):
    if request.method=="POST":
        uid = request.POST['uid']
        cust_id = request.POST['customid']
        item = request.POST['item']
        price= request.POST['price']
        r=Restaurant.objects.filter(uid=uid)[0]
        if Cart.objects.filter(uid=uid).exists():
            a=Cart.objects.filter(uid=uid).order_by('-order_no')[0]
            c = Cart(uid=int(uid),name=r.hotel,order_no=((a.order_no)+1),cust_id=cust_id,item=item,price=price)
            c.save()
        else: 
            c = Cart(uid=int(uid),name=r.hotel,order_no=1,cust_id=cust_id,item=item,price=price)
            c.save()
    return redirect('restaurant',restaurant_id=int(uid))

def viewcart(request):
    if request.method=="POST":
        status=request.POST['status']
        a=Cart.objects.filter(cust_id=request.user.email)
        d=Rec_Order.objects.filter(cust_id=request.user.email)
        d.delete()
        for i in a:
            p = Rec_Order(uid=i.uid,name=i.name,order_no=i.order_no,cust_id=i.cust_id,item=i.item,price=i.price)
            p.save()
            if Order.objects.filter(uid=i.uid).exists():
                b=Order.objects.filter(uid=i.uid).order_by('-order_no')[0]
                c = Order(uid=i.uid,order_no=((b.order_no)+1),cust_id=i.cust_id,item=i.item,price=i.price,status=status)
                c.save()
            else: 
                c = Order(uid=i.uid,order_no=1,cust_id=i.cust_id,item=i.item,price=i.price,status=status)
                c.save()
        a.delete()
        return redirect('last_order')
        
    a=Cart.objects.filter(cust_id=request.user.email).order_by('order_no')
    context = {
        'contents':a
    }
    return render(request,'customer/cart.html',context)

def delcart(request):
    if request.method=="POST":
        order_no = request.POST['order_no']
        b = Cart.objects.filter(cust_id = request.user.email).order_by('order_no')
        for i in b:
            if int(i.order_no) == int(order_no):
                i.delete()
            if int(i.order_no) > int(order_no):
                c = Cart(uid=i.uid,name=i.name,order_no=((i.order_no)-1),cust_id=i.cust_id,item=i.item,price=i.price)
                c.save()
                i.delete()
    return redirect('viewcart')

def last_order(request):
    a = Rec_Order.objects.filter(cust_id = request.user.email).order_by('order_no')
    context = {
        'contents':a,
    }
    return render(request,'customer/last_order.html',context)