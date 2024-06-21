from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.conf import settings

class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    product = GenericForeignKey('content_type', 'object_id')
    quantity = models.PositiveIntegerField(default=1)


class TFTs(models.Model):
    def get_content_type(self):
        return ContentType.objects.get_for_model(self.__class__)
    
    name = models.CharField(max_length=200, blank=False, null=False)
    description = models.TextField(blank=True)
    price= models.DecimalField(max_digits=10, decimal_places=2)
    stock= models.BooleanField(default=False)
    image= models.ImageField(null=True, blank=True)
    image_url = models.URLField(null=True, blank= True)
    cart_items = GenericRelation(CartItem, related_query_name='product')

    def __str__(self):
        return f"{self.name} {self.description}"
    

class GamingPC(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    description = models.TextField(blank=True)
    price= models.DecimalField(max_digits=10, decimal_places=2)
    stock= models.BooleanField(default=False) 
    image= models.ImageField(null=True, blank=True)
    image_url = models.URLField(null=True, blank= True)
    cart_items = GenericRelation(CartItem, related_query_name='product')


    def __str__(self):
        return f"{self.name} {self.description}"
    
class Laptops(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    description = models.TextField(blank=True)
    price= models.DecimalField(max_digits=10, decimal_places=2)
    stock= models.BooleanField(default=False)
    image= models.ImageField(null=True, blank=True)
    image_url = models.URLField(null=True, blank= True)
    cart_items = GenericRelation(CartItem, related_query_name='product')


    def __str__(self):
        return f"{self.name} {self.description}"
    
class Accessories(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    description = models.TextField(blank=True)
    price= models.DecimalField(max_digits=10, decimal_places=2)
    stock= models.BooleanField(default=False)
    image= models.ImageField(null=True, blank=True)
    image_url = models.URLField(null=True, blank= True)
    cart_items = GenericRelation(CartItem, related_query_name='product')


    def __str__(self):
        return f"{self.name} {self.description}"

class GraphicsCard(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    description = models.TextField(blank=True)
    price= models.DecimalField(max_digits=10, decimal_places=2)
    stock= models.BooleanField(default=False)
    image= models.ImageField(null=True, blank=True)
    image_url = models.URLField(null=True, blank= True)
    cart_items = GenericRelation(CartItem, related_query_name='product')


    def __str__(self):
        return f"{self.name} {self.description}"
    
class ComputerParts(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    description = models.TextField(blank=True)
    price= models.DecimalField(max_digits=10, decimal_places=2)
    stock= models.BooleanField(default=False)
    image= models.ImageField(null=True, blank=True)
    image_url = models.URLField(null=True, blank= True)
    cart_items = GenericRelation(CartItem, related_query_name='product')

    

    def __str__(self):
        return f"{self.name} {self.description}"

