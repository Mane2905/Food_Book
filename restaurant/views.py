
from django.shortcuts import render
from .models import Menu,Restaurant,Order
# Create your views here.
def index(request):
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
    context={
        'cont':address[0],
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
        c = Order(uid=a.uid,order_no=a.order_no,cust_id=a.cust_id,item=a.item,price=a.price,status="Accepted")
        c.save()
        a.delete()
    contents=Order.objects.filter(uid=request.user.id).order_by('order_no')
    context={
        'contents':contents,
        
    }
    
    return render(request,'restaurant/order.html',context)