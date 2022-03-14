from django.shortcuts import render,redirect
from restaurant.models import Restaurant,Menu,Order
from .models import Cart,Rec_Order,Customer

# Create your views here.
var=0
diction={}
def address_cust(request):
    if request.method=="POST":
        global var
        global diction
        if Customer.objects.filter(uid = request.user.id).exists():
            a = Customer.objects.get(uid = request.user.id)
            a.delete()
        uid = request.user.id
        address_1= request.POST['Address_1']
        address_2= request.POST['Address_2']
        city= request.POST['City']
        pin= request.POST['Pin']
        phone= request.POST['Phone']
        '''default = request.POST['Default']
        if default == "true":
            cust = Customer.objects.filter(uid=uid).filter(default = "true")
            for c in cust:
                d=Customer(uid=request.user.id,address_1=c.address_1,address_2=c.address_2,city=c.city,pin=c.pin,phone=c.phone,default="false")
                d.save()
                c.delete()'''
        p = Customer(uid=uid,address_1=address_1,address_2=address_2,city=city,pin=pin,phone=phone)
        p.save()
        d=Rec_Order.objects.filter(cust_id=request.user.email)
        d.delete()
        if var == 1:
            a=Cart.objects.filter(cust_id=request.user.email)
            for i in a:
                p = Rec_Order(uid=i.uid,name=i.name,order_no=i.order_no,cust_id=i.cust_id,item=i.item,price=i.price)
                p.save()
                if Order.objects.filter(uid=i.uid).exists():
                    b=Order.objects.filter(uid=i.uid).order_by('-order_no')[0]
                    c = Order(uid=i.uid,order_no=((b.order_no)+1),cust_id=i.cust_id,item=i.item,price=i.price,status=diction['status'],address_1=address_1,address_2=address_2,city=city,pin=pin,phone=phone)
                    c.save()
                else: 
                    c = Order(uid=i.uid,order_no=1,cust_id=i.cust_id,item=i.item,price=i.price,status=diction['status'],address_1=address_1,address_2=address_2,city=city,pin=pin,phone=phone)
                    c.save()
            a.delete()
        elif var == 2:
            b = Restaurant.objects.filter(uid = diction['uid'])[0]
            p = Rec_Order(uid=diction['uid'],name=b.hotel,order_no=1,cust_id=diction['cust_id'],item=diction['item'],price=diction['price'])
            p.save()
            if Order.objects.filter(uid=diction['uid']).exists():
                a=Order.objects.filter(uid=diction['uid']).order_by('-order_no')[0]
                c = Order(uid=diction['uid'],order_no=((a.order_no)+1),cust_id=diction['cust_id'],item=diction['item'],price=diction['price'],status=diction['status'],address_1=address_1,address_2=address_2,city=city,pin=pin,phone=phone)
                c.save()
            else: 
                c = Order(uid=diction['uid'],order_no=1,cust_id=diction['cust_id'],item=diction['item'],price=diction['price'],status=diction['status'],address_1=address_1,address_2=address_2,city=city,pin=pin,phone=phone)
                c.save()
        var = 0
        diction = {}
        return redirect('last_order')

    address = Customer.objects.filter(uid=request.user.id)
    if Customer.objects.filter(uid = request.user.id).exists():
        context={
            'cont':address[0],
        }
    else:
        context={
            'cont':address,
        }
    return render(request,'customer/address.html',context)

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
        global var
        global diction
        status=request.POST['status']
        uid = request.POST['uid']
        cust_id = request.POST['customid']
        item = request.POST['item']
        price= request.POST['price']
        diction = {
            'status':status,
            'uid': uid,
            'cust_id':cust_id,
            'item':item,
            'price':price
        }
        var = 2
        return redirect('address')
        

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
        global var
        global diction
        status=request.POST['status']
        var = 1
        diction = {
            'status':status
        }
        return redirect('address')
        
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
