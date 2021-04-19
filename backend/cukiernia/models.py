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
    category_id = models.ForeignKey('Category', on_delete=models.PROTECT)
    recommended = models.BooleanField()

class RelatedProductJunction(models.Model):
    related_first = models.ManyToManyField(Product, related_name='related_first')
    related_second = models.ManyToManyField(Product, related_name='related_second')

class ProductPhoto(models.Model):
    product_id = models.ForeignKey('Product', on_delete=models.PROTECT)
    main_photo = models.BooleanField()
    url = models.ImageField(upload_to =RandomFileName('uploads/products/'))

class TextBox(models.Model):
    name_pl = models.TextField(max_length=255)
    name_en = models.TextField(max_length=255)
    product_id = models.ForeignKey('Product', on_delete=models.CASCADE)
    is_required = models.BooleanField()
    max_length = models.IntegerField()


class ComboBox(models.Model):
    name_pl = models.CharField(max_length=50)
    name_en = models.CharField(max_length=50)
    product_id = models.ForeignKey('Product', on_delete=models.CASCADE)
    is_required = models.BooleanField()


class Calendar(models.Model):
    name_pl = models.CharField(max_length=50)
    name_en = models.CharField(max_length=50)
    product_id = models.ForeignKey('Product', on_delete=models.CASCADE)
    is_required = models.BooleanField()

class ComboBoxValue(models.Model):
    text_pl = models.CharField(max_length=50)
    text_en = models.CharField(max_length=50)
    combo_box_id = models.ForeignKey('ComboBox', on_delete=models.CASCADE)

class Category(models.Model):
    name_pl = models.CharField(max_length=50)
    name_en = models.CharField(max_length=50)

class Carousel(models.Model):
    enabled = models.BooleanField()

class CarouselPhoto(models.Model):
    url = models.ImageField(upload_to =RandomFileName('uploads/carousel/'))

class Order(models.Model):
    status_choices_pl = [
        ('zlozone', 'Złożone'),
        ('oplacone', 'Opłacone'),
        ('zrealizowane', 'Zrealizowane')
    ]
    status_choices_en = [
        ('ordered', 'Ordered'),
        ('paid', 'Paid'),
        ('complete', 'Complete')
    ]
    delivery_methods = [
        ('odbior', 'Odbiór osobisty'),
        ('kurier', 'Kurier')
    ]
    order_date = models.DateField()
    delivery_date = models.DateField()
    status_pl = models.CharField(choices=status_choices_pl, max_length=50)
    status_en = models.CharField(choices=status_choices_en, max_length=50)
    street = models.CharField(max_length=100, blank=True, default="")
    postcode = models.CharField(max_length=6, blank=True, default="")
    city = models.CharField(max_length=50, blank=True, default="")
    courier_note = models.TextField(max_length=500)
    dealer_note = models.TextField(max_length=500)
    delivery = models.CharField(choices=delivery_methods, max_length=50)
    price = models.FloatField()
    products = models.ManyToManyField(Product)
    user = CurrentUserField()



@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False,**kwargs):
    if created:
        Token.objects.create(user=instance)
    if not created:
        Token.objects.get(user=instance).delete()
        Token.objects.create(user=instance)