from django.db import models

# Create your models here.
class Customer(models.Model):
    uid = models.IntegerField(
        blank=False
    )
    address_1 = models.TextField(blank=False)
    address_2 = models.TextField(blank=False,default="")
    city = models.TextField(blank=False)
    pin= models.TextField(blank=False)
    phone = models.TextField(blank=False)
    def __int__(self):
        return self.uid

class Cart(models.Model):
    uid = models.IntegerField(blank=False)
    name = models.TextField(blank = False)
    order_no = models.IntegerField(blank=False)
    cust_id = models.EmailField(max_length=255)
    item = models.TextField(blank=False)
    price = models.TextField(blank=False,default="100")
    def __str__(self):
        return self.cust_id

class Rec_Order(models.Model):
    uid = models.IntegerField(blank=False)
    name = models.TextField(blank = False)
    order_no = models.IntegerField(blank=False)
    cust_id = models.EmailField(max_length=255)
    item = models.TextField(blank=False)
    price = models.TextField(blank=False,default="100")
    def __str__(self):
        return self.cust_id