from django.contrib import admin
from Restaurant.models import Restaurants

# Register your models here.
class RestaurantsAdmin(admin.ModelAdmin):
    list_display=['name']
admin.site.register(Restaurants,RestaurantsAdmin)
