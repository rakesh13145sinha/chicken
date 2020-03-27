from django.shortcuts import render

# Create your views here.
def order_detail(request):
    return render(request,'templates/order/Order_page.html')

def orderupdate (request):
    pass
