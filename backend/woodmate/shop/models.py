from django.db import models

class Customer(models.Model):
    cid = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=10)
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name

class Sales(models.Model):
    sid = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name

class DeliveryMan(models.Model):
    dm_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=10)
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)

class ProductType(models.Model):
    ptype_id = models.AutoField(primary_key=True)
    ptype_name = models.CharField(max_length=30)

    def __str__(self):
        return self.ptype_name

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_type = models.ForeignKey(ProductType, on_delete=models.PROTECT)
    product_name = models.CharField(max_length=100)
    product_desc = models.CharField(max_length=150)
    price = models.IntegerField()
    stock = models.IntegerField()
    modifier = models.ForeignKey(Sales, on_delete=models.PROTECT)

    def __str__(self):
        return self.product_name

class Order(models.Model):
    oid = models.AutoField(primary_key=True)
    payment = models.CharField(max_length=50)
    status = models.CharField(max_length=30)
    date = models.DateField()
    total_price = models.IntegerField(null=True, blank=True)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    sales = models.ForeignKey(Sales, on_delete=models.PROTECT, null=True, blank=True)
    deliveryman = models.ForeignKey(DeliveryMan, on_delete=models.PROTECT, null=True, blank=True)

class OrderList(models.Model):
    line_id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    unit = models.IntegerField()
    price = models.IntegerField()
    total_price = models.IntegerField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

class Cart(models.Model):
    cart_id = models.AutoField(primary_key=True)
    cid = models.ForeignKey(Customer, on_delete=models.CASCADE)
    pid = models.ForeignKey(Product, on_delete=models.CASCADE)
    unit = models.IntegerField()

class Address(models.Model):
    address_id = models.AutoField(primary_key=True)
    address_desc = models.CharField(max_length=500)
    district = models.CharField(max_length=50)
    area = models.CharField(max_length=50)
    province = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=5)
    cid = models.ForeignKey(Customer, on_delete=models.CASCADE)

class Feedback(models.Model):
    text = models.CharField(max_length=500)
