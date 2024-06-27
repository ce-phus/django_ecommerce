from django.shortcuts import render
from .cart import Cart


def cart_detail(request):
    cart = Cart(request)
    productstring= ''

    for item in cart:
        product = item['product']
        url = '/%s/%s/' % (product.category.slug, product.slug)
        b = "{'id': '%s', 'title': '%s', 'price': '%s', 'quantity': '%s', 'total_price': '%s', 'thumbnail': '%s', 'url': '%s', 'num_available': '%s'}," % (product.id, product.title, product.price, item['quantity'], item['total_price'], product.get_thumbnail, url, product.num_available)

        productsstring = productstring + b

    if request.user.is_authenticated:
        username = request.user.username
        email = request.user.email
        phone = request.user.BillingAddress.phone_number
        pin_code = request.user.BillingAddress.pin
        house_no = request.BillingAddress.house_no
        city = request.user.BillingAddress.city
        landmark = request.user.BillingAddress.landmark

    else:
        username = email = phone = pin_code = house_no = city = landmark = ''

    context = {
        'cart': cart,
        'username': username,
        'email': email,
        'phone': phone,
        'pin_code': pin_code,
        'house_no': house_no,
        'city' : city,
        'landmark': landmark,
        'productsstring': productsstring.rstrip(',')
    }
    return render(request, 'products/cart.html', context)

def success(request):
    cart = Cart(request)
    cart.clear

    return render(request, 'products/success.html')