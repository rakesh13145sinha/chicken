from django.urls import path
from Restaurant import views
urlpatterns = [
    path('name/', views.home,),
    path('open/restaurant/',views.new_restaurant),
   
    
]
