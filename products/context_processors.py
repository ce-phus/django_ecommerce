from .models import Cart
from django.db import models

def cart_item_count(request):
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
        item_count = cart.items.aggregate(total=models.Sum('quantity'))['total'] or 0
    else:
        item_count = 0
    return {'cart_item_count': item_count}