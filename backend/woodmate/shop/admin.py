from django.contrib import admin
from django.contrib.auth.models import Permission

# Register your models here.
from shop.models import *

admin.site.register(Permission)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_id', 'product_name', 'stock', 'product_type_id']
    list_per_page = 10
    search_fields = ['product_name']

admin.site.register(Product, ProductAdmin)

class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ['ptype_id', 'ptype_name']
    list_per_page = 10
    search_fields = ['ptype_name']

admin.site.register(ProductType, ProductTypeAdmin)

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['id', 'text']
    list_per_page = 10
    search_fields = ['text']

admin.site.register(Feedback, FeedbackAdmin)
