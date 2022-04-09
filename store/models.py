from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL

# Create your models here.

class Collection(models.Model):
    title = models.CharField(max_length = 255)
    featured_product = models.ForeignKey('Products' , on_delete = SET_NULL, null = True, related_name = '+')

class Promotions(models.Model):
    description = models.CharField(max_length = 255)
    discount = models.FloatField()

class Products(models.Model):
    title = models.CharField(max_length = 255)
    slug = models.SlugField()
    description = models.TextField()
    unit_price = models.DecimalField(max_digits = 9, decimal_places = 2)
    inventory = models.IntegerField() 
    last_update = models.DateTimeField(auto_now = True)
    collection = models.ForeignKey(Collection, on_delete = models.PROTECT)
    promotions = models.ManyToManyField(Promotions)

class Customers(models.Model):
    MEMBERSHIP_BRONZE = 'B'
    MEMBERSHIP_SILVER = 'S'
    MEMBERSHIP_GOLD = 'G'
    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_BRONZE , 'Bronze'),
        (MEMBERSHIP_SILVER , 'Silver'),
        (MEMBERSHIP_GOLD , 'Gold'),
        ]
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.EmailField(unique = True)
    phone = models.CharField(max_length = 12)
    birth_date = models.DateField(null = True)
    membership = models.CharField(max_length = 1, choices = MEMBERSHIP_CHOICES, default = MEMBERSHIP_BRONZE)

class Orders(models.Model):
    PAYMENT_PENDING_STATUS = 'P'
    PAYMENT_COMPLETE_STATUS = 'C'
    PAYMENT_FAILED_STATUS = 'F'

    PAYMENT_STATUS_CHOICES = [
        (PAYMENT_PENDING_STATUS , 'Pending'),
        (PAYMENT_COMPLETE_STATUS , 'Complete'),
        (PAYMENT_FAILED_STATUS , 'Failed'),
        ]
    placed_at = models.DateTimeField(auto_now_add = True)
    payment_status = models.CharField(max_length = 1, choices = PAYMENT_STATUS_CHOICES, default = PAYMENT_PENDING_STATUS)

    customer = models.ForeignKey(Customers, on_delete = models.PROTECT)


class OrderItems(models.Model):
    order = models.ForeignKey(Orders, on_delete = models.PROTECT)
    product = models.ForeignKey(Products, on_delete = models.PROTECT)
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits = 9, decimal_places = 2)

class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add = True)

class CartItems(models.Model):
    cart = models.ForeignKey(Cart, on_delete = CASCADE)
    product = models.ForeignKey(Products, on_delete = CASCADE)
    quantity = models.PositiveSmallIntegerField()


class Address(models.Model):
    street = models.CharField(max_length = 255)
    city = models.CharField(max_length = 255)
    customers = models.ForeignKey(Customers, on_delete = CASCADE)

