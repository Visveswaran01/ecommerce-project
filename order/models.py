from django.db import models
from core.models import Consumer
from product.models import Product

# Create your models here.

class ShippingAddress(models.Model):
    address = models.TextField()
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255, blank=True)
    default = models.BooleanField(default=False)

class Order(models.Model):
    
    ORDERED = 'ordered'
    SHIPPED = 'shipped'
    STATUS_CHOICES = (
            (ORDERED, 'Ordered'),
            (SHIPPED, 'Shipped')
        )
    
    user = models.ForeignKey(Consumer, on_delete=models.CASCADE,blank=True,null=True)
    shipping_address = models.OneToOneField(ShippingAddress, on_delete=models.CASCADE)
    order_placed_at = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)
    paid_amount = models.IntegerField(default=0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=ORDERED)

    class Meta:
        ordering = ["-order_placed_at",]

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,blank=True,null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL,blank=True,null=True)
    quantity = models.IntegerField(default=0)
    price = models.IntegerField()