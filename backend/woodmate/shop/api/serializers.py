from rest_framework import serializers
from shop.models import *
from django.contrib.auth.models import User, Group

class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = ('cid', 'first_name', 'last_name', 'email', 'phone_number')

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = ('oid', 'payment', 'status', 'date', 'total_price', 'customer', 'sales', 'deliveryman')

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ('product_id', 'product_type', 'product_name', 'product_desc', 'product_pic', 'price', 'stock')

class ProductTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductType
        fields = ('ptype_id', 'ptype_name')

class SalesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sales
        fields = ('sid', 'first_name', 'last_name')

class DeliveryManSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DeliveryMan
        fields = ('dm_id', 'first_name', 'last_name', 'phone_number')

class OrderListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OrderList
        fields = ('line_id','product', 'unit', 'price', 'total_price', 'order')

class CartSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cart
        fields = ('cart_id', 'cid', 'pid', 'unit')

class AddressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Address
        fields = ('address_id', 'address_desc', 'district', 'area', 'province', 'postal_code', 'cid')

class FeedbackSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Feedback
        fields = ('id', 'text')
