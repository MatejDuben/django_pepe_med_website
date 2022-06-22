from django.db import models
from django.contrib.auth.models import User
from pathlib import Path
from django.utils.text import slugify
# Create your models here.


class Customer(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True, blank=True)
	email = models.CharField(max_length=200, null=True, blank=True)
	device = models.CharField(max_length=200, null=True, blank=True)

	def __str__(self):
		if self.name:
			name = self.name
		else:
			name = self.device
		return str(name)



class ProductsInfo(models.Model):
  title = models.CharField(max_length=200)
  product_type = models.CharField(max_length=100) #med, sviecka, betlehem
  description = models.TextField(max_length=500)
  price = models.FloatField(default=0)
  slug = models.SlugField(null=True,blank=True)
  image = models.ImageField(upload_to='products_images')
  image_one = models.ImageField(upload_to='products_images', blank=True, null=True)
  image_two = models.ImageField(upload_to='products_images', blank=True, null=True)

  def __str__(self):
    return self.title

  def save(self, *args, **kwargs):
    if not self.slug:
      self.slug = slugify(self.title)
    super().save(*args,**kwargs)

class ShopItem(models.Model):
  item = models.ForeignKey(ProductsInfo, on_delete=models.CASCADE)
  ammout = models.IntegerField(default=0)
  who_has_item = models.ForeignKey(Customer, on_delete=models.CASCADE)
  

  def __str__(self):
    name = f'{str(self.item)}, {str(self.who_has_item)}'
    return name


  def get_total_sum(self):
    return float(self.item.price)*int(self.ammout)

  def get_item_img(self):
    return self.item.image

  def get_img_name(self):
    img_name = Path(str(self.item.image)).name
    return img_name

  def get_title(self):
    return self.item.title
  
  def get_price(self):
    return self.item.price
 
