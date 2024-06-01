from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User, AbstractUser


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(blank=True, null=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:  # Generate slug only if it's not already set
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


    def __str__(self):
        return self.name    
    
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    body = models.TextField()
    quantity = models.IntegerField()
    slug = models.SlugField()
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name) 
        super().save(*args, **kwargs)  

    def __str__(self):
        return self.name    
    

class Review(models.Model):
    mark = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
