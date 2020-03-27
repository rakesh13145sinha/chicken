from django.urls import path
from Authorization import views

urlpatterns = [
    path('',views.signup)
]   
