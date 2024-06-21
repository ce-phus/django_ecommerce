from django.contrib import admin
from .models import GamingPC, GraphicsCard, Accessories, Laptops, TFTs, ComputerParts, CartItem, Cart

class GamingPCAdmin(admin.ModelAdmin):
    list_display= ("id", "name", "description", "price", "stock", "image")

class GraphicsCardAdmin(admin.ModelAdmin):
    list_display= ("id", "name", "description", "price", "stock", "image")

class AccessoriesAdmin(admin.ModelAdmin):
    list_display= ("id", "name", "description", "price", "stock", "image")

class LaptopsAdmin(admin.ModelAdmin):
    list_display= ("id", "name", "description", "price", "stock", "image")

class TFTsAdmin(admin.ModelAdmin):
    list_display= ("id", "name", "description", "price", "stock", "image")

class ComputerPartsAdmin(admin.ModelAdmin):
    list_display= ("id", "name", "description", "price", "stock", "image")

admin.site.register(GamingPC, GamingPCAdmin)
admin.site.register(GraphicsCard, GraphicsCardAdmin)
admin.site.register(Accessories, AccessoriesAdmin)
admin.site.register(Laptops, LaptopsAdmin)
admin.site.register(TFTs, TFTsAdmin)
admin.site.register(ComputerParts, ComputerPartsAdmin)
admin.site.register(Cart)
admin.site.register(CartItem)




