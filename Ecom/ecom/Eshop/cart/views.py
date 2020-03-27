# from django.shortcuts import render,HttpResponseRedirect
# from django.urls import reverse
# from django.contrib.auth.decorators import login_required
# from django.contrib.sessions.models import Session


# from cart.models import Cart
# from product.models import Product  

# # Create your views here.
# @login_required
# def cart_view(request):
#     try:
#         the_id = request.session['cart_id']
#     except:
#         the_id=None
#     if the_id:
#         cart=Cart.objects.get(id=the_id)
#         context={"cart":cart}
#     else:
#         empty_massage="YOUR CART IS EMPTY KEEP SHOPPING"
#         context={"empty":True,"empty_massage":empty_massage}

#     return render(request,'templates/cart/Order_page.html',context)
# @login_required
# def update_cart_view(request,slug):
#     try:
#         request.session['cart_id']
#     except:
#         new_cart = Cart()
#         new_cart.save()
#         request.session['cart_id'] = new_cart.id
#         the_id = new_cart.id
#     cart=Cart.objects.get(id=the_id)     
#     try:
#         product=Product.objects.get(slug=slug)
#     except Product.DoesNotExist:
#         pass
#     except:
#         pass
#     if not product in cart.product.all():
#         cart.product.add(product)
        
#     else:
#         cart.product.remove(product)

#     new_total=0.00
#     for item in cart.product.all():
#         new_total += float(item.price)
#     request.session['item_total']=cart.product.count()
#     print()
#     cart.total=new_total
#     cart.save()

#     return HttpResponseRedirect(reverse('cart'))
