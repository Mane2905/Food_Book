from django.db import models

# Create your models here.
class Cart(models.Model):
<<<<<<< HEAD
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
=======
    uid = models.TextField(blank=False)
>>>>>>> dee17ae37cd145b15c0b16ca4915060bd0735f21
    order_no = models.IntegerField(blank=False)
    cust_id = models.EmailField(max_length=255)
    item = models.TextField(blank=False)
    price = models.TextField(blank=False,default="100")
    def __str__(self):
        return self.cust_id