from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserUpdateForm, BillingAddressForm, OrderForm
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