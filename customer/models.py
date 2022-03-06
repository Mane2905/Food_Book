from django.db import models

# Create your models here.
class Cart(models.Model):
    uid = models.TextField(blank=False)
    order_no = models.IntegerField(blank=False)
    cust_id = models.EmailField(max_length=255)
    item = models.TextField(blank=False)
    price = models.TextField(blank=False,default="100")
    def __str__(self):
        return self.cust_id