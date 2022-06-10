from django.db import models
from user.models import User

# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=20)

class Product(models.Model):
    name = models.CharField(max_length=20)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    disc = models.TextField()
    price = models.CharField(max_length=20)
    stock = models.CharField(max_length=20)

class OrderStatus(models.Model):
    order_status = models.CharField(max_length=20)

class ProductOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order_qty = models.CharField(max_length=20)

class UserOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    order_time = models.CharField(max_length=20)
    total_price = models.CharField(max_length=20)
    valid = models.CharField(max_length=20)
