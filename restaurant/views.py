
from django.shortcuts import render,redirect
from .models import Menu,Restaurant,Order
# Create your views here.
def index_rest(request):
    if request.method=="POST":
        if Restaurant.objects.filter(uid = request.user.id).exists():
            a = Restaurant.objects.get(uid = request.user.id)
            a.delete()
        uid = request.user.id
        hotel = request.POST['Hotel']
        address_1= request.POST['Address_1']
        address_2= request.POST['Address_2']
        city= request.POST['City']
        pin= request.POST['Pin']
        phone= request.POST['Phone']
        c = Restaurant(hotel=hotel,uid = uid,address_1=address_1,address_2=address_2,city=city,pin=pin,phone=phone)
        c.save()
    address = Restaurant.objects.filter(uid=request.user.id)
    if Restaurant.objects.filter(uid = request.user.id).exists():
        context={
            'cont':address[0],
        }
    else:
        context={
            'cont':address
        }
    return render(request,'restaurant/index.html',context)
def menu(request):
    contents=Menu.objects.order_by('-price').filter(uid=request.user.id)
    
    
    context={
        
        'contents':contents,
    }
    
    if request.method=="POST":
        uid = request.user.id
        item= request.POST['item']
        price=request.POST['price']
        b = Menu(uid = uid,item=item, price=price)
        b.save()
    return render(request,'restaurant/menu.html',context)

def order(request):
    if request.method=="POST":
        order_no=request.POST['order_no']
        a = Order.objects.filter(uid=request.user.id).filter(order_no=order_no)[0]
        c = Order(uid=a.uid,order_no=a.order_no,cust_id=a.cust_id,item=a.item,price=a.price,status="Accepted",address_1=a.address_1,address_2=a.address_2,city=a.city,pin=a.pin,phone=a.phone)
        c.save()
        a.delete()
    contents=Order.objects.filter(uid=request.user.id)#.order_by('order_no')
    context={
        'contents':contents,
        
    }
    
    return render(request,'restaurant/order.html',context)

def customer_order(request,order_no):
    content = Order.objects.filter(uid = request.user.id).filter(order_no = order_no)
    context = {
        'content':content[0]
    }
    return render(request,'restaurant/sp_order.html',context)

def deliver(request):
    if request.method=="POST":
        order_no=request.POST['order_no']
        b = Order.objects.filter(uid = request.user.id).order_by('order_no')
        for i in b:
            if int(i.order_no) == int(order_no):
                i.delete()
            if int(i.order_no) > int(order_no):
                c = Cart(uid=i.uid,name=i.name,order_no=((i.order_no)-1),cust_id=i.cust_id,item=i.item,price=i.price)
                c.save()
                i.delete()
    return redirect('order')