# from django.shortcuts import render
# from django.contrib.auth.decorators import login_required
# from product.models import Product,ProductImage,Slider




# # Create your views here.
# def Front_Page(request):
#     item=Product.objects.all()
    
#     context={
#         'item':item,
        
#     }
    
#     return render(request,'templates/shoper/home.html',context)
# @login_required
# def python_view(request):
#     list_display=Product.objects.all()
#     return render(request,'templates/shoper/category.html',{'list_display':list_display})
# #logout 
# def logout(request):
#     return render(request,'templates/shoper/logout.html')

