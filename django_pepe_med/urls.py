"""django_pepe_med URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls import url

from django.conf import settings 
from django.conf.urls.static import static 

from main_app.views import home, contact, sent_email, sent_email_err, card_page, update_item, sent_email_on_card, page_404, apiterapia_page, thankForBuying, update_item_via_products_page, info_page_how_to_buy

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', home, name='home_page'),
    re_path(r'^$', home, name="home_page"),
    re_path(r'^produkty/', include('main_app.products_urls'), name='products_page'),
    re_path(r'^kontakt/', contact, name='contact_page'),
    re_path(r'^odoslanie-emailu/',sent_email, name='email_sent'),
    re_path(r'^odoslanie-emailu-zlihalo/',sent_email_err, name='email_sent_err'),
    re_path(r'^moj-zoznam/$', card_page, name='card_page'),
    re_path(r'^apiterapia/', apiterapia_page, name='apiterapia_page'),
    path('updateItem/', update_item),
    path('updateViaProductsPage/', update_item_via_products_page),
    path('sentMsgCard/', sent_email_on_card),
    re_path(r'^error-page/', page_404),
    path('objednavkaVybavena/', thankForBuying, name='order_completed'),
    path('ako-objednat-tovar/', info_page_how_to_buy, name='how_to_buy_page'),



]

if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)