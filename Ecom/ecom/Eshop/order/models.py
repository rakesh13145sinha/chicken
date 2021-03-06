from django.db import models
from product.models import Product

# Create your models here.
class OrderItem(models.Model):
    product         =models.ForeignKey(Product,null=True,blank=True,on_delete=models.CASCADE)
    quantity        =models.IntegerField()
    timestamp       =models.DateTimeField(auto_now=False ,auto_now_add=True)
    update          =models.DateTimeField(auto_now=True,auto_now_add=False)



class Order(models.Model):
    product         =models.ManyToManyField(OrderItem,null=True,blank=True)
    total           =models.DecimalField(max_digits=100,decimal_places=2,default=00.00)
    timestamp       =models.DateTimeField(auto_now=False ,auto_now_add=True)
    update          =models.DateTimeField(auto_now=True,auto_now_add=False)
    active          =models.BooleanField(default=True)
    def __unicode__(self):
        return "cart id: %s"(self.id)