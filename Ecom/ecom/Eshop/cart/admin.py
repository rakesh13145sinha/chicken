from django.contrib import admin

# Register your models here.
from cart.models import Cart
class CartAdmin(admin.ModelAdmin):
    class Meta:
        model=Cart
admin.site.register(Cart,CartAdmin)
