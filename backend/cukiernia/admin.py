from django.contrib import admin
from .models import Product, ProductPhoto, TextBox, ComboBox, ComboBoxValue, OnDemandRetail, InstantRetail
from .models import Calendar, Category, Carousel, CarouselPhoto, RelatedProductJunction, Order, OrderStatus, Delivery, Decoration
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.

@admin.register(Product)
class ProductAdmin(SummernoteModelAdmin):
    list_display = ['code', 'name_pl','name_en', 'price' ,'category', 'recommended']
    ordering = ['name_pl', 'name_en', 'price']
    summernote_fields = '__all__'

@admin.register(OnDemandRetail)
class OnDemandRetailAdmin(SummernoteModelAdmin):
    list_display = ['product', 'production_time']
    ordering = ['product']

@admin.register(InstantRetail)
class InstantDemandRetailAdmin(SummernoteModelAdmin):
    list_display = ['product', 'quantity_available']
    ordering = ['product']

@admin.register(RelatedProductJunction)
class RelatedProductJunctionAdmin(admin.ModelAdmin):
    list_display = ['id']
    ordering = ['id']

@admin.register(ProductPhoto)
class ProductPhotoAdmin(admin.ModelAdmin):
    list_display = ['product', 'main_photo']
    ordering = ['product', 'url']

@admin.register(TextBox)
class TextBoxAdmin(admin.ModelAdmin):
    list_display = ['name_pl', 'name_en', 'product']
    ordering = ['product', 'name_pl', 'name_en']

@admin.register(ComboBox)
class ComboBoxAdmin(admin.ModelAdmin):
    list_display = ['name_pl', 'name_en', 'product']
    ordering = ['product', 'name_pl', 'name_en']

@admin.register(Calendar)
class CalendarAdmin(admin.ModelAdmin):
    list_display = ['name_pl', 'name_en',]
    ordering = ['name_pl', 'name_en', 'id']

@admin.register(ComboBoxValue)
class ComboBoxValueAdmin(admin.ModelAdmin):
    list_display = ['text_pl', 'text_en', 'combo_box']
    ordering = ['combo_box', 'text_pl', 'text_en']

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

@admin.register(Decoration)
class DecorationAdmin(admin.ModelAdmin):
    list_display = ['id', 'name_pl', 'value_pl', 'price']
    ordering = ['name_pl', 'value_pl']