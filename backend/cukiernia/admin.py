from django.contrib import admin
from .models import Product, ProductPhoto, TextBox, ComboBox, ComboBoxValue
from .models import Calendar, Category, Carousel, CarouselPhoto, RelatedProductJunction


# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['code', 'name_pl','name_en', 'price' ,'category_id', 'recommended']
    ordering = ['name_pl', 'name_en', 'price']

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
    list_display = ['name', 'product_id']
    ordering = ['product_id', 'name']

@admin.register(ComboBox)
class ComboBoxAdmin(admin.ModelAdmin):
    list_display = ['name', 'product_id']
    ordering = ['product_id', 'name']

@admin.register(Calendar)
class CalendarAdmin(admin.ModelAdmin):
    list_display = ['name']
    ordering = ['name', 'id']

@admin.register(ComboBoxValue)
class ComboBoxValueAdmin(admin.ModelAdmin):
    list_display = ['text', 'combo_box_id']
    ordering = ['combo_box_id', 'text']

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