from django.db import models
from core.models import Consumer
import math

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()

    class Meta:
        ordering = ('name',)
    
    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,blank=True,null=True)
    img = models.ImageField(blank=True,null=True)
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField(blank=True,null=True)
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self) -> str:
        return self.name
    
    def get_rating(self):
        reviews_total = 0

        for review in self.reviews.all():
            reviews_total += review.rating
        
        if reviews_total > 0:
            return math.ceil(reviews_total / self.reviews.count())
        
        return 0

class Review(models.Model):
    user = models.ForeignKey(Consumer, related_name='ureviews', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='reviews', on_delete=models.CASCADE)
    rating = models.IntegerField(default=3)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)