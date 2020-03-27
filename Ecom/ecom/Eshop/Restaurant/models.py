from django.db import models

# Create your models here.

class Restaurants(models.Model):
    name              =models.CharField(max_length=100)
    image             =models.ImageField(upload_to='restaurants/images/')
    sub_text          =models.CharField(max_length=50)
    price             =models.DecimalField(decimal_places=2,max_digits=100,null=True,blank=True)
    cost              =models.DecimalField(decimal_places=2,max_digits=100,null=True,blank=True)
    rating            =models.DecimalField(decimal_places=2,max_digits=100,null=True,blank=True)
    discripsion       =models.TextField(max_length=500)
    address           =models.TextField(max_length=500)
    offer             =models.CharField(max_length=50)
    slug              =models.SlugField()
    time              =models.DateTimeField(auto_now_add=True,auto_now=False)
    update            =models.DateTimeField(auto_now_add=False, auto_now=True)
    activate          =models.BooleanField(default=True)
    start_date        =models.DateTimeField(auto_now_add=False,auto_now=False,null=True,blank=True)
    end_date          =models.DateTimeField(auto_now_add=False,auto_now=False,null=True,blank=True)
    time              =models.DateTimeField(auto_now_add=True,auto_now=False)
    def __str__(self):
        return self.name
   
