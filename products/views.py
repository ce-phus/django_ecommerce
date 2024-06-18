from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse, HttpResponseNotAllowed, HttpResponse
from django.views import View
from .models import TFTs, GamingPC, GraphicsCard, Laptops, Accessories, ComputerParts
from django.contrib.auth.mixins import UserPassesTestMixin
from .forms import TFTsForm, ComputerPartsForm, LaptopsForm, AccessoriesForm, GamingPCForm, GraphicsCardForm

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
        tft = get_object_or_404(TFTs, pk)
        return render(request, 'products/tfts_detail.html', {'tft':tft}) 

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
