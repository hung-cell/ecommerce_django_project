from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):

    name = models.CharField(max_length=200)
    price = models.FloatField()
    digital = models.BooleanField(default=False, null=True, blank=True)
    image = models.ImageField(null=True, blank=True, default='placeholder.png')
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, default=False, null=True)

    description = models.TextField(
        default="This is a product description", null=True, blank=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        orderItems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderItems])
        return total

    def get_cart_items(self):
        orderItems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderItems])
        return total

    def shipping(self):
        shipping = False
        orderItems = self.orderitem_set.all()
        for i in orderItems:
            if i.product.digital == False:
                shipping = True
        return shipping


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total


class ShippingInfo(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=200, null=False)
    zip_code = models.CharField(max_length=200, null=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
