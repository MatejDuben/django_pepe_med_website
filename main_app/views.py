from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from email.mime.image import MIMEImage
from pathlib import Path

from django.core.mail import message, send_mail, EmailMultiAlternatives, EmailMessage
from django.template.loader import render_to_string
from django.utils import html
from django.utils.html import strip_tags

from django.views.decorators.csrf import csrf_protect

from django.http import JsonResponse
import json

from django.conf import settings
# Create your views here.
from main_app.models import ProductsInfo, ShopItem, Customer

import os

def home(request):

  if request.method == 'POST':

    subject = request.POST.get('email')
    message = request.POST.get('message')
    send_mail(
      subject=subject,
      message=message,
      from_email=subject,
      recipient_list=['@gmail.com'],
      fail_silently=False
    )
    return redirect(to='email_sent')

  return render(request, 'index.html')

def products(request):
  all_products = ProductsInfo.objects.all()   
  context = {
    'products':all_products
  }
  return render(request, 'products_page.html', context=context)


def update_item_via_products_page(request):
  #this_user mi da pouzivatela ktory je bud prihlaseny alebo je to len cislo zariadenia(cookie) ktore je na stranke
  #pomocou neho mozem interagovat s userom
  try:
    this_user = request.user.customer
  except:
    device = request.COOKIES['device']
    this_user, created = Customer.objects.get_or_create(device=device)
  try:
    data = json.loads(request.body)

    product_id = data['productId']
    page_action = data['action']

    specific_product = ProductsInfo.objects.get(id=product_id)

    if page_action == 'plus':
      if ShopItem.objects.filter(item=specific_product, who_has_item=this_user).exists():
        shop_item = get_object_or_404(ShopItem, item=specific_product, who_has_item=this_user)
        shop_item.ammout += 1
        shop_item.save()
      else:
        shop_item = ShopItem(item=specific_product, who_has_item=this_user, ammout=1)
        shop_item.save()
    


    return JsonResponse('updated..', safe=False)
  except:
    return render('info_pages/page_404.html')





def product(request, product_name):
  try:
    specific_product = ProductsInfo.objects.get(slug=product_name)
    is_added = False
  except:
    return render(request, 'info_pages/page_404.html')

  try:
    if request.method == "POST":
      is_added = True
      try:
        this_user = request.user.customer
      except:
        device = request.COOKIES['device']
        this_user, created = Customer.objects.get_or_create(device=device)


      if ShopItem.objects.filter(item=specific_product, who_has_item=this_user).exists():
        shop_item = get_object_or_404(ShopItem, item=specific_product, who_has_item=this_user)
        shop_item.ammout += 1
        shop_item.save()
        #print(shop_item.get_total_sum())
      else:
        shop_item = ShopItem(who_has_item=this_user, item=specific_product, ammout=1)
        shop_item.save()

      context = {
        'product_title': specific_product.title,
        'product_desc': specific_product.description,
        'product_price': specific_product.price,

        'product_img': specific_product.image,
        'product_img_one': specific_product.image_one,
        'product_img_two': specific_product.image_two,
        'product_id': specific_product.id,

        'added': is_added
      }


      return render(request, 'product_view_page.html', context=context)
  except:
    return render(request, 'info_pages/page_404.html')


  context = {
    'product_title': specific_product.title,
    'product_desc': specific_product.description,
    'product_price': specific_product.price,

    'product_img': specific_product.image,
    'product_img_one': specific_product.image_one,
    'product_img_two': specific_product.image_two,
    'product_id': specific_product.id,

    'added': is_added

  }
  return render(request, 'product_view_page.html', context=context)

def contact(request):

  if request.method == "POST":
    subject_email = request.POST.get('email')
    customer_name = request.POST.get('customer_name')
    subject_phone_number = request.POST.get('phone_num')
    message = request.POST.get('message')



    # try:
    #   if customer_name != '' and subject_email != '' and subject_phone_number != '' and message != '':
    #     send_mail(
    #       subject=f'email: {subject_email}, číslo: {subject_phone_number}',
    #       message=message,
    #       from_email=subject_email,
    #       recipient_list=['1pepe.med1@gmail.com'],
    #       fail_silently=False
    #     )
    #     print(f"{customer_name},{subject_email}, {subject_phone_number}, {message}")
    #     return redirect(to='email_sent')
    # except:
    #   return redirect(to='email_sent_err')



  return render(request, 'contact_page.html')



def info_page_how_to_buy(request):

  return render(request, 'info_pages/how_to_buy.html')



def apiterapia_page(request):

  return render(request, 'apiterapia_page.html')



def sent_email(request):
  return render(request, 'info_pages/email_sent.html')

def sent_email_err(request):
  return render(request, 'info_pages/email_sent_err.html')




def card_page(request):

  try:
    this_user = request.user.customer
    user_card = ShopItem.objects.filter(who_has_item=this_user).all()
    print(this_user)
    context = {
      "userCard": user_card,
    }
    return render(request, 'card_list.html', context)
    #ked je pouzivatel prihlaseny tak neodosle sa email - pouzivatel sa nebude prihlasovat bude fungovat len ako device
  except:   #ak je uzivatel neprihlaseny je len device tak sa email odosle
    try:
      device = request.COOKIES['device']
      this_user, created = Customer.objects.get_or_create(device=device)
      user_card = ShopItem.objects.filter(who_has_item=this_user).all()
      print(this_user)
    
      #get total sum to pay
      def get_total_sum_to_pay():
        items_price = []
        total_sum_to_pay = 0

        for i in user_card:
          items_price.append(i.get_total_sum())

        for item_price in items_price:
          total_sum_to_pay += item_price
          
        return total_sum_to_pay

        
        


      #toto presmeruje na vybavenu ojednavku
      if request.method == 'POST':
        customer_name=request.POST.get('userName')
        customer_last_name= request.POST.get('userLastName')
        customer_email=request.POST.get('userEmail')
        customer_number_phone=request.POST.get('userNum')
        customer_massage=request.POST.get('userMsg')


        try:
          #ak nieje jedno z policok vyplnene tak sa neopdosle
          if customer_name != '' and customer_last_name != '' and customer_email  != '' and customer_number_phone != '':

            send_mail(
              subject=f'Meno: {customer_name} {customer_last_name} email: {customer_email}, číslo: {customer_number_phone}',
              message=f"Produkty: {[ i.item for i in user_card]} - {[i.ammout for i in user_card]} \nSuma celkom: {get_total_sum_to_pay()} \n Správa: {customer_massage}",
              from_email=customer_email,
              recipient_list=['@gmail.com'],
              fail_silently=False
            )
            

            #send email to user           
            recipient = customer_email
            sender = settings.EMAIL_HOST_USER 
            image_names = []
            image_path = []  
            for i in user_card:
              i_n = i.get_img_name()    #i_n -> image name
              image_names.append(i_n)
              image_path.append(os.path.join('D:\programing in HTML\django_pepe_med/media/products_images', i_n))
            print('image paths: ', image_path)
            print('IMAGES FILE NAME: ', image_names)
            
        
            html_content = render_to_string('info_pages/email_template.html', {'userCard':user_card, 'name': customer_name, "image_names":image_names, "total_sum_to_pay": get_total_sum_to_pay()})
            subject = "Informácie o objednávke z pepemed.sk"
            text_message = f"Email with a nice embedded image {image_names}."
              

            # the function for sending an email
            email = EmailMultiAlternatives(subject=subject, body=text_message, from_email=sender, to=[recipient])
            
            email.attach_alternative(html_content, "text/html")
            email.content_subtype = 'html'  
            email.mixed_subtype = 'related'
            
            for img_path in image_path:
              with open(img_path, mode='rb') as f:
                image = MIMEImage(f.read(), _subtype="jpg")
                email.attach(image)
                image.add_header('Content-ID', f"<{Path(img_path).name}>")
    
            #odosle email---->
            email.send()

        

            #delete sruff from card
            mail_sent = True
            if mail_sent:
              user_card.delete()

            return redirect(to='order_completed')

        except:
          mail_sent = False
          return redirect(to='email_sent_err')


      context = {
        "userCard": user_card,
      }


      return render(request, 'card_list.html', context)
    except:   #ak nebude device tak nepojde na zoznam ale 404 page
      return render(request, 'info_pages/page_404.html')




@csrf_protect
def sent_email_on_card(request):      #send email to pepemed  toto je v card_page view spravene
  mail_sent = False
  try:
    this_user = request.user.customer
  except:
    device = request.COOKIES['device']
    this_user, created = Customer.objects.get_or_create(device=device)

  user_card = ShopItem.objects.filter(who_has_item=this_user).all()

  #counting all prices and return total sum to pay
  user_totalsum_to_pay = 0
  for i in user_card:
    user_totalsum_to_pay += i.get_total_sum()


  data = json.loads(request.body)

  customer_name=data['user_name']
  customer_last_name=data['user_last_name']
  customer_email=data['user_emali']
  customer_number_phone=data['user_num']
  customer_massage=data['user_massage']

  try:
    #ak nieje jedno z policok vyplnene tak sa neopdosle
    if customer_name != '' and customer_last_name != '' and customer_email  != '' and customer_number_phone != '':
      print('Poslal sa Email')
      send_mail(
        subject=f'Meno: {customer_name} {customer_last_name} email: {customer_email}, číslo: {customer_number_phone}',
        message=f"Produkty: {[ i.item for i in user_card]} - {[i.ammout for i in user_card]} \nSuma celkom: {user_totalsum_to_pay} \n Správa: {customer_massage}",
        from_email=customer_email,
        recipient_list=['1pepe.med1@gmail.com'],
        fail_silently=False
      )

      #send email to user

      # mail_sent = True

      # if mail_sent:
      #   user_card.delete()

    return JsonResponse('poslal sa Email', safe=False)

  except:
    mail_sent = False
    print('neposlal sa Email')
    return JsonResponse('neposlal sa Email', safe=False)


def thankForBuying(request):

  try:
    this_user = request.user.customer
  except:
    device = request.COOKIES['device']
    this_user, created = Customer.objects.get_or_create(device=device)
  user_card = ShopItem.objects.filter(who_has_item=this_user).all()

  return render(request, 'info_pages/thank_for_buying.html')
  #return render(request, 'info_pages/email_template.html')



def update_item(request):
  data = json.loads(request.body)

  productId = data['productId']
  action = data['action']

  item = ShopItem.objects.get(id=productId)

  if action == "plus":
    item.ammout += 1
    item.save()
  elif action == "minus":
    item.ammout -= 1
    item.save()
  if item.ammout == 0:
    item.delete()

  return JsonResponse('Item was added', safe=False)





def page_404(request):
  render(request, 'info_pages/page_404.html')

