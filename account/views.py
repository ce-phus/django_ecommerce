from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserUpdateForm, BillingAddressForm, OrderForm, PasswordUpdateForm
from django.utils import timezone
from .models import BillingAddress, OrderModel
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, 'account/index.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = make_password(form.cleaned_data['password'])
            user.last_login = timezone.now()
            user.save()
            messages.success(request, f'Your Account has been created! You are now logged in')
            return redirect('login')
        
    else:
        form = UserRegistrationForm()
    return render(request, 'account/register.html', {'form': form})
# Account views
@login_required
def account_details(request):
    return render(request, 'account/account_details.html', {'user': request.user})

@login_required
def update_account(request):
    if request.method == 'PUT':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        password_form = PasswordUpdateForm(request.PUT)
        if user_form.is_valid() and password_form.is_valid():
            user = user_form.save(commit=False)
            if password_form.cleaned_data['password']:
                user.password = make_password(password_form.cleaned_data['password'])
            user.save()
            return redirect('account/account_details')
        
    else:
        user_form = UserUpdateForm(instance=request.user)
        password_form = PasswordUpdateForm()

    return render(request, 'account/update_account.html', {
        'user_form': user_form,
        'password_form': password_form
    })

@login_required
def delete_account(request):
    if request.method == 'POST':
        request.user.delete()
        return redirect('index')
    return render(request, 'delete')

# Address Views
@login_required
def address_list(request):
    addresses = BillingAddress.objects.filter(user=request.user)
    return render(request, 'address/address_list.html', {'addresses': addresses})

@login_required
def address_detail(request, pk):
    address = BillingAddress.objects.get(pk=pk)
    return render(request, 'address_detail.html', {'address': address})

@login_required
def create_address(request):
    if request.method == 'POST':
        form = BillingAddressForm(request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            address.user = request.user
            address.save()
            return redirect('address_list')
    else:
        form = BillingAddressForm()
    return render(request, 'address/create_address.html', {'form': form})

@login_required
def update_address(request, pk):
    address = BillingAddress.objects.get(pk=pk)
    if request.method == 'PUT':
        form = BillingAddressForm(request.PUT, instance=address)
        if form.is_valid():
            form.save()
            return redirect('address_list')
    else:
        form = BillingAddressForm(instance=address)
    return render(request, 'address/update_address.html', {'form': form})

@login_required
def delete_address(request, pk):
    address = BillingAddress.objects.get(pk=pk)
    if request.method == 'POST':
        address.delete()
        return redirect('address_list')
    return render(request, 'address/delete_address.html', {'address': address})

@login_required
def order_list(request):
    if request.user.is_staff:
        orders = OrderModel.objects.all()
    else:
        orders = OrderModel.objects.filter(user=request.user)
    return render(request, 'order/order_list.html', {'orders': orders})

@login_required
def change_order_status(request, pk):
    if not request.user.is_staff:
        return redirect('home')
    
    order = OrderModel.objects.get(pk=pk)
    if request.method == 'POST':
        order.is_delivered = request.POST.get('is_delivered') == 'on'
        order.delivered_at = timezone.now() if order.is_delivered else None
        order.save()
        return redirect('order_list')
    return render(request, 'order/change_order_status.html', {'order': order})