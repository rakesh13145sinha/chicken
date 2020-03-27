from django.shortcuts import render
from Restaurant.models import Restaurants
from product.models import Product,ProductImage,Slider
# Create your views here.
def home(request):
    item=Restaurants.objects.all()
    slide=Slider.objects.all()
    context={
        'item':item,
        'slide':slide,
            }
    return render(request,'templates/restaurant/index.html',context)

def new_restaurant(request):
    return render(request,'templates/restaurant/AddShop.html')


