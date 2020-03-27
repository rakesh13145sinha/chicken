from django.contrib import admin
from order.models import OrderItem,Order
# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    class Meta:
        model=Order
admin.site.register(Order,OrderAdmin)
class OrderItemAdmin(admin.ModelAdmin):
    class Meta:
        model=OrderItem
admin.site.register(OrderItem,OrderItemAdmin)