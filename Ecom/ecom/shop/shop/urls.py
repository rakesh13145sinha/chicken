"""shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from shopapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('java/',views.java),
    path('python/',views.python),
    path('sql/',views.sql),
    path('accounts/',include('django.contrib.auth.urls')),
    path('form/',views.student_form),   
    path('accouts/logout/',views.logout),
    path('signup/',views.signup),
    path('list/',views.display),
    path('signfor/',views.class_signup),
   # path('accounts/password_change/',views.password_change),
    #path('accounts/password_change_done/',views.password_done)

]
