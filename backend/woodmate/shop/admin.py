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

class SalesAdmin(admin.ModelAdmin):
    list_display = ['sid', 'first_name', 'last_name']
    list_per_page = 10
    search_fields = ['first_name']

class DeliveryManAdmin(admin.ModelAdmin):
    list_display = ['dm_id', 'first_name', 'last_name']
    list_per_page = 10
    search_fields = ['first_name']

admin.site.register(DeliveryMan, DeliveryManAdmin)

admin.site.register(Sales, SalesAdmin)

class CartAdmin(admin.ModelAdmin):
    list_display = ['cart_id', 'cid', 'pid', 'unit']
    list_per_page = 10
    list_filter = ['cid']

admin.site.register(Cart, CartAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display = ['oid', 'payment', 'status', 'date', 'total_price', 'customer']
    list_per_page = 10
    list_filter = ['status']

admin.site.register(Order, OrderAdmin)

class OrderListAdmin(admin.ModelAdmin):
    list_display = ['line_id', 'order']
    list_per_page = 10

admin.site.register(OrderList, OrderListAdmin)

class AddressInline(admin.TabularInline):
    model = Address
    extra = 0

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['cid', 'first_name', 'last_name']
    list_per_page = 10
    search_fields = ['first_name']
    inlines = [AddressInline]

admin.site.register(Customer, CustomerAdmin)

class AddressAdmin(admin.ModelAdmin):
    list_display = ['address_id', 'cid']
    list_per_page = 10
    list_filter = ['cid']

admin.site.register(Address, AddressAdmin)