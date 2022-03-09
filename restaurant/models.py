from django.db import models
class Restaurant(models.Model):
    uid = models.IntegerField(
        blank=False
    )
    hotel = models.TextField(blank=False,default="")
    address_1 = models.TextField(blank=False)
    address_2 = models.TextField(blank=False,default="")
    city = models.TextField(blank=False)
    pin= models.TextField(blank=False)
    phone = models.TextField(blank=False)

    def __str__(self):
        return self.uid
class Menu(models.Model):
    uid = models.IntegerField(
        blank=False
    )
    item = models.TextField(blank=False)
    price = models.TextField(blank=False,default="100")

    def __str__(self):
        return self.uid
class Order(models.Model):
    uid = models.IntegerField(blank=False)
    order_no = models.IntegerField(blank=False)
    cust_id = models.EmailField(max_length=255)
    item = models.TextField(blank=False)
    price = models.TextField(blank=False,default="100")
    status = models.TextField(blank=False)
    def __str__(self):
        return self.cust_id