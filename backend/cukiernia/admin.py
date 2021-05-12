from django.contrib import admin
from .models import Product, ProductPhoto, TextBox, ComboBox, ComboBoxValue, OnDemandRetail, InstantRetail
from .models import Calendar, Category, Carousel, CarouselPhoto, RelatedProductJunction, Order, OrderStatus, Delivery
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.

@admin.register(Product)
class ProductAdmin(SummernoteModelAdmin):
    list_display = ['code', 'name_pl','name_en', 'price' ,'category_id', 'recommended']
    ordering = ['name_pl', 'name_en', 'price']
    summernote_fields = '__all__'

@admin.register(OnDemandRetail)
class OnDemandRetailAdmin(SummernoteModelAdmin):
    list_display = ['product_id', 'production_time']
    ordering = ['product_id']

@admin.register(InstantRetail)
class InstantDemandRetailAdmin(SummernoteModelAdmin):
    list_display = ['product_id', 'quantity_available']
    ordering = ['product_id']

@admin.register(RelatedProductJunction)
class RelatedProductJunctionAdmin(admin.ModelAdmin):
    list_display = ['id']
    ordering = ['id']

@admin.register(ProductPhoto)
class ProductPhotoAdmin(admin.ModelAdmin):
    list_display = ['product_id', 'main_photo']
    ordering = ['product_id', 'url']

@admin.register(TextBox)
class TextBoxAdmin(admin.ModelAdmin):
    list_display = ['name_pl', 'name_en', 'product_id']
    ordering = ['product_id', 'name_pl', 'name_en']

@admin.register(ComboBox)
class ComboBoxAdmin(admin.ModelAdmin):
    list_display = ['name_pl', 'name_en', 'product_id']
    ordering = ['product_id', 'name_pl', 'name_en']

@admin.register(Calendar)
class CalendarAdmin(admin.ModelAdmin):
    list_display = ['name_pl', 'name_en',]
    ordering = ['name_pl', 'name_en', 'id']

@admin.register(ComboBoxValue)
class ComboBoxValueAdmin(admin.ModelAdmin):
    list_display = ['text_pl', 'text_en', 'combo_box_id']
    ordering = ['combo_box_id', 'text_pl', 'text_en']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name_pl', 'name_en']
    ordering = ['name_pl', 'name_en']

@admin.register(Carousel)
class CarouselAdmin(admin.ModelAdmin):
    list_display = ['id', 'enabled']
    ordering = ['id']

@admin.register(CarouselPhoto)
class CarouselPhotoAdmin(admin.ModelAdmin):
    list_display = ['url']
    ordering = ['id']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id']
    ordering = ['id']

@admin.register(OrderStatus)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'name_pl', 'name_en']
    ordering = ['id', 'name_pl', 'name_en']

@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name_pl', 'name_en', 'price']
    ordering = ['id', 'name_pl', 'name_en']