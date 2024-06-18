from django import forms
from .models import TFTs, GamingPC, GraphicsCard, ComputerParts, Laptops, Accessories

class TFTsForm(forms.ModelForm):
    class Meta:
        model = TFTs
        fields = ['name', 'description', 'price', 'stock', 'image']


class GamingPCForm(forms.ModelForm):
    class Meta:
        model = GamingPC
        fields = ['name', 'description', 'price', 'stock', 'image']

class ComputerPartsForm(forms.ModelForm):
    class Meta:
        model = ComputerParts
        fields = ['name', 'description', 'price', 'stock', 'image']

class GraphicsCardForm(forms.ModelForm):
    class Meta:
        model = GraphicsCard
        fields = ['name', 'description', 'price', 'stock', 'image']

class AccessoriesForm(forms.ModelForm):
    class Meta:
        model = Accessories
        fields = ['name', 'description', 'price', 'stock', 'image']

class LaptopsForm(forms.ModelForm):
    class Meta:
        model = Laptops
        fields = ['name', 'description', 'price', 'stock', 'image']