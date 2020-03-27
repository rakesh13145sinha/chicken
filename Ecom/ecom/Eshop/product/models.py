from django.db import models
from Restaurant.models import Restaurants

# Create your models here.
class Product(models.Model):
    name            =models.CharField(max_length=100)
    model           =models.CharField(max_length=50)
    price           =models.DecimalField(decimal_places=2,max_digits=100,null=True,blank=True)
    discripsion     =models.TextField(max_length=500)
    pieces          =models.IntegerField(default=False)
    slug            =models.SlugField()
    time            =models.DateTimeField(auto_now_add=True,auto_now=False)
    update          =models.DateTimeField(auto_now_add=False, auto_now=True)
    activate        =models.BooleanField(default=True)
    def __str__(self):
        return self.name
        
    def get_price(self):
        return self.price   

class ProductImage(models.Model):
    product          =models.ForeignKey(Product,on_delete=models.CASCADE)
    restaurant       =models.ForeignKey(Restaurants,on_delete=models.CASCADE,default=True)
    image            =models.ImageField(upload_to='products/images/')
    featured         =models.BooleanField(default=False)
    thumbnail        =models.BooleanField(default=True)
    active           =models.BooleanField(default=True)
    updated          =models.DateTimeField(auto_now=True, auto_now_add=False)
    def __unicode__(self):
        return self.product.id


class Slider(models.Model):
    image             =models.ImageField(upload_to='slider/image/')
    header_text       =models.CharField(max_length=200,null=True,blank=True)
    text              =models.CharField(max_length=300,null=True,blank=True)
    
    active            =models.BooleanField(default=True)
    updated           =models.DateTimeField(auto_now=True, auto_now_add=False)
    time              =models.DateTimeField(auto_now_add=True,auto_now=False)
    featured          =models.BooleanField(default=False)
    start_date        =models.DateTimeField(auto_now_add=False,auto_now=False,null=True,blank=True)
    end_date          =models.DateTimeField(auto_now_add=False,auto_now=False,null=True,blank=True)

    def __unicode__(self):
        return str(self.id)