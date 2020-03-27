from django.urls import path
from order import views
urlpatterns = [

    path('detail/<int:id>',views.order_detail),
    
    
]
