from django.db import models
from django.dispatch import receiver
from django_currentuser.db.models import CurrentUserField
from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save
from django.conf import settings
from .helpers import RandomFileName

# Create your models here.

class Product(models.Model):
    '''
    Class depicting product.
    '''
    code = models.CharField(max_length=15)
    price = models.FloatField()
    name_pl = models.CharField(max_length=50)
    name_en = models.CharField(max_length=50)
    product_description_pl = models.TextField()
    product_description_en = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.PROTECT)
    recommended = models.BooleanField()

class OnDemandRetail(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, unique=True)
    production_time = models.IntegerField(default=1)

class InstantRetail(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, unique=True)
    quantity_available = models.IntegerField(default=0)


class RelatedProductJunction(models.Model):
    related_first = models.ManyToManyField(Product, related_name='related_first')
    related_second = models.ManyToManyField(Product, related_name='related_second')

class ProductPhoto(models.Model):
    product = models.ForeignKey('Product', on_delete=models.PROTECT)
    main_photo = models.BooleanField()
    url = models.ImageField(upload_to =RandomFileName('uploads/products/'))

class TextBox(models.Model):
    name_pl = models.TextField(max_length=255)
    name_en = models.TextField(max_length=255)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    is_required = models.BooleanField()
    max_length = models.IntegerField()


class ComboBox(models.Model):
    name_pl = models.CharField(max_length=50)
    name_en = models.CharField(max_length=50)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    is_required = models.BooleanField()


class Calendar(models.Model):
    name_pl = models.CharField(max_length=50)
    name_en = models.CharField(max_length=50)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    is_required = models.BooleanField()

class ComboBoxValue(models.Model):
    text_pl = models.CharField(max_length=50)
    text_en = models.CharField(max_length=50)
    combo_box = models.ForeignKey('ComboBox', on_delete=models.CASCADE)
    price_factor = models.DecimalField(max_digits=6, decimal_places=2)

class Category(models.Model):
    name_pl = models.CharField(max_length=50)
    name_en = models.CharField(max_length=50)

class Carousel(models.Model):
    enabled = models.BooleanField()

class CarouselPhoto(models.Model):
    url = models.ImageField(upload_to =RandomFileName('uploads/carousel/'))

class Decoration(models.Model):
    name_pl = models.CharField(max_length=50)
    name_en = models.CharField(max_length=50)
    value_pl = models.CharField(max_length=50)
    value_en = models.CharField(max_length=50)
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=6, decimal_places=2)

class Order(models.Model):
    order_date = models.DateField()
    delivery_date = models.DateField()
    status = models.ForeignKey('OrderStatus', on_delete=models.PROTECT)
    street = models.CharField(max_length=100, blank=True, default="")
    postcode = models.CharField(max_length=6, blank=True, default="")
    city = models.CharField(max_length=50, blank=True, default="")
    courier_note = models.TextField(max_length=500)
    dealer_note = models.TextField(max_length=500)
    delivery = models.ForeignKey('Delivery', on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    products = models.ManyToManyField(Product)
    user = CurrentUserField()

class OrderStatus(models.Model):
    name_pl = models.CharField(max_length=25)
    name_en = models.CharField(max_length=25)

class Delivery(models.Model):
    name_pl = models.CharField(max_length=25)
    name_en = models.CharField(max_length=25)
    price = models.DecimalField(max_digits=6, decimal_places=2)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False,**kwargs):
    if created:
        Token.objects.create(user=instance)
    if not created:
        Token.objects.get(user=instance).delete()
        Token.objects.create(user=instance)