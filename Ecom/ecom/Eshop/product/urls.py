from django.urls import path
from product import views
urlpatterns = [


    path('item/<int:id>/',views.product_by_restaurant),
    path('add/<int:id>',views.add_to_cart),
    
]
