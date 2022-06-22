from django.contrib import admin
from django.urls import path, re_path

from main_app.views import home, product,products


urlpatterns = [
  path('', products, name="products_page"),
  re_path(r'^(?P<product_name>[-\w]+)/$', product, name="product_page"),
  

]
