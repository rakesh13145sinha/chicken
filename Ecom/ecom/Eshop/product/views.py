from django.shortcuts import render
from product.models import Product,ProductImage
from Restaurant.models import Restaurants
from order.models import Order,OrderItem



# Create your views here.

def product_by_restaurant(request,id):
    restaurant=Restaurants.objects.get(id=id)
    product=ProductImage.objects.filter(restaurant=restaurant)
    context={
            'restaurant':restaurant,
            'product':product,
            
            }
    return render(request,'templates/product/cart1.html',context)


def add_to_cart(request,id):
    product_name=Product.objects.get(id=id)
    product_image=ProductImage.objects.filter(product=product_name)
    print(porcut_image)

    print(product_name)
    product_name=Product.objects.get(id=id)
    product_image=ProductImage.objects.get(product=product_name)
    if request.method=="POST":
        first=request.POST['example1']
        cart=OrderItem.objects.create(quantity=first,product=product_name)
        cart.save()
        
        return render(request,'templates/order/order_page.html',{
            'product_name':product_name,
            'cart':cart,
            'product_image':product_image,
        })
        







