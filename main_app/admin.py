from django.contrib import admin
from main_app.models import ProductsInfo, Customer, ShopItem
# Register your models here.
admin.site.register(Customer)
admin.site.register(ProductsInfo)
admin.site.register(ShopItem)
#admin.site.register(ShopCard)