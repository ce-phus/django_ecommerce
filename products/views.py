from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseNotAllowed, HttpResponse
from django.views import View
from .models import TFTs, GamingPC, GraphicsCard, Laptops, Accessories, ComputerParts, Cart, CartItem
from django.contrib.auth.mixins import UserPassesTestMixin
from .forms import TFTsForm, ComputerPartsForm, LaptopsForm, AccessoriesForm, GamingPCForm, GraphicsCardForm
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseBadRequest

# Create your views here.

class IsAdminUserMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff
    
class TFTsView(View):
    def get(self, request):
        tfts = TFTs.objects.all()
        return render(request, 'products/tfts_list.html', {'tfts': tfts})

class TFTsDetailView(View):
    def get(self, request, pk):
        tft = get_object_or_404(TFTs, pk=pk)
        return render(request, 'products/tft_detail.html', {'tft':tft}) 

class TFTsCreateView(IsAdminUserMixin, View):
    def get(self, request):
        form = TFTsForm()
        return render(request, 'products/tfts_form.html', {'form': form})
    
    def post(self, request):
        form = TFTsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('tfts_list')
        return render(request, 'products/tfts_form.html', {'form': form})
    
class TFTsEditView(IsAdminUserMixin, View):
    def get(self, request, pk):
        tft = get_object_or_404(TFTs, pk=pk)
        form = TFTsForm(instance=tft)
        return render(request, 'products/tfts_form.html', {'form': form})

    def put(self, request, pk):
        tft = get_object_or_404(TFTs, pk=pk)
        form = TFTsForm(request.PUT, request.FILES, instance=tft)
        if form.is_valid():
            form.save()
            return redirect('tfts_detail', pk=pk)
        return render(request, 'products/tfts_form.html', {'form': form})
    
class TFTsDeleteView(IsAdminUserMixin, View):
    def get(self, request, pk):
        tft = get_object_or_404(TFTs, pk=pk)
        tft.delete()
        return redirect('tfts_list')


@login_required
def add_to_cart(request, product_id):
    if request.method == "POST":
        product_type = request.POST.get('product_type')

        product_model = {
            'tfts': TFTs,
            'gamingpc': GamingPC,
            'laptops': Laptops,
            'accessories': Accessories,
            'graphicscard': GraphicsCard,
            'computerparts': ComputerParts,
        }.get(product_type)

        if product_model is None:
            return JsonResponse({'error': 'Invalid product type'}, status=400)

        product = get_object_or_404(product_model, id=product_id)
        cart, created = Cart.objects.get_or_create(user=request.user)
        content_type = ContentType.objects.get_for_model(product)

        cart_item, created = CartItem.objects.get_or_create(
            cart=cart,
            content_type=content_type,
            object_id=product.id,
            defaults={'quantity': 1}
        )

        if not created:
            cart_item.quantity += 1
            cart_item.save()

        cart_items_count = cart.items.count()

        return JsonResponse({'cart_items_count': cart_items_count})

    return JsonResponse({'error': 'Invalid request method'}, status=405)
    

@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    cart_item.delete()
    return redirect('cart_detail')

@login_required
def update_cart_quantity(request, item_id, quantity):
    cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    cart_item.quantity = quantity
    cart_item.save()
    return redirect('cart_detail')

def cart_detail(request):
    try:
        cart = Cart.objects.get(user=request.user)
        cart_items = cart.items.all()
        context = {
            'cart': cart,
            'cart_items': cart_items,
        }
        return render(request, 'products/cart_detail.html', context)
    except Cart.DoesNotExist:
        return render(request, 'products/cart_detail.html', {'cart': None})


def cart_summary(request):
    if request.method == 'GET':
        try:
            cart = Cart.objects.get(user=request.user)
            cart_items = cart.items.all()
            total_quantity = sum(item.quantity for item in cart_items)
            data = {
                'total_quantity': total_quantity,
            }
            return JsonResponse(data)
        except Cart.DoesNotExist:
            return JsonResponse({'error': 'Cart not found'}, status=404)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
    
def cart_item_count(request):
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
        return {'cart_item_count': cart.items.count()}
    return {'cart_item_count': 0}
