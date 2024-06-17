from django import forms
from django.contrib.auth.models import User
from .models import BillingAddress, OrderModel
from django.core.validators import RegexValidator

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input-field'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input-field'}))

    class Meta:
        model = User
        fields = ["username", "email", "password"]
        widgets = {
            "username" : forms.TextInput(attrs={"class" : "input-field"}),
            "email" : forms.EmailInput(attrs={"class" : "input-field"})
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match")
        
        return cleaned_data
    
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

class PasswordUpdateForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input-field'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input-field'}))

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        
        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match")
        return cleaned_data

class BillingAddressForm(forms.ModelForm):
    class Meta:
        model = BillingAddress
        fields = ['username', 'phone_number', 'pin_code', 'house_no', 'landmark', 'city', 'state']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'input-field'}),
            'phone_number': forms.TextInput(attrs={'class': 'input-field'}),
            'pin_code': forms.TextInput(attrs={'class': 'input-field'}),
            'house_no': forms.TextInput(attrs={'class': 'input-field'}),
            'landmark': forms.TextInput(attrs={'class': 'input-field'}),
            'city': forms.TextInput(attrs={'class': 'input-field'}),
            'state': forms.TextInput(attrs={'class': 'input-field'}),
        }

class OrderForm(forms.ModelForm):
    class Meta:
        model = OrderModel
        fields = ['username', 'ordered_item', 'phone_number', 'address', 'total_price', 'is_delivered']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'input-field'}),
            'ordered_item': forms.TextInput(attrs={'class': 'input-field'}),
            'phone_number': forms.TextInput(attrs={'class': 'input-field'}),
            'address': forms.TextInput(attrs={'class': 'input-field'}),
            'total_price': forms.NumberInput(attrs={'class': 'input-field'}),
            'is_delivered': forms.CheckboxInput(attrs={'class': 'input-field'}),
        }
