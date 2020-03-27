from django.contrib import admin
from product.models import Product,ProductImage,Slider

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display=['name','model','price','id']
    list_editable=['price']
    #date_hierarchy='timestamp'
    #list_filter=['price','activate']

class SliderAdmin(admin.ModelAdmin):
    class Meta:
        model=Slider
class ProductImageAdmin(admin.ModelAdmin):
    list_display=['id','image']
admin.site.register(ProductImage,ProductImageAdmin)
admin.site.register(Slider,SliderAdmin)
admin.site.register(Product,ProductAdmin)
