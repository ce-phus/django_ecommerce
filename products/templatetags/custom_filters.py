from django import template

register = template.Library()

@register.filter
def mul(value, arg):
    return value * arg

@register.filter
def sum_total(cart_items):
    total = 0
    for item in cart_items:
        total += item.quantity * item.product.price
    return total