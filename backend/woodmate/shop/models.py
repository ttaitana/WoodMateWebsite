from django.db import models

class Customer(models.Model):
    cid = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=10)
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)

class ProductType(models.Model):
    ptype_id = models.IntegerField()
    ptype_name = models.CharField(max_length=30)

class Product(models.Model):
    product_id = models.IntegerField(primary_key=True)
    product_type = models.ForeignKey(ProductType, on_delete=models.PROTECT)
    product_name = models.CharField(max_length=100)
    product_desc = models.CharField(max_length=150)
    price = models.IntegerField()
    stock = models.IntegerField()

class Order(models.Model):
    oid = models.IntegerField(primary_key=True)
    payment = models.CharField(max_length=50)
    status = models.CharField(max_length=30)
    date = models.DateField()
    total_price = models.IntegerField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

class OrderList(models.Model):
    line_id = models.IntegerField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    unit = models.IntegerField()
    price = models.IntegerField()
    total_price = models.IntegerField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

class Sales(models.Model):
    sid = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

class DeliveryMan(models.Model):
    dm_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=10)
