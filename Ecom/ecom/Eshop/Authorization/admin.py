from django.contrib import admin
from Authorization.models import Identification

# Register your models here.
class IdentificationAdmin(admin.ModelAdmin):
    list_display=['user_name','email']
admin.site.register(Identification,IdentificationAdmin)