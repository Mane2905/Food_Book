from django.shortcuts import render
from restaurant.models import Restaurant,Menu,Order
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
        if Order.objects.filter(uid=uid).exists():
            a=Order.objects.filter(uid=uid).order_by('order_no')[0]
            c = Order(uid=uid,order_no=((a.order_no)+1),cust_id=cust_id,item=item,price=price,status=status)
            c.save()
        else: 
            c = Order(uid=uid,order_no=1,cust_id=cust_id,item=item,price=price,status=status)
            c.save()
    return render(request,'customer/order.html')