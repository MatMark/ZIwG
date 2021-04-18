from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Product, ProductPhoto, TextBox, ComboBox, ComboBoxValue
from .models import Calendar, Category, Carousel, CarouselPhoto, RelatedProductJunction


class UserSerializer(serializers.HyperlinkedModelSerializer):
    '''
    This class is serializer for User model
    '''
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    '''
    This class is serializer for Group model
    '''
    class Meta:
        model = Group
        fields = ['url', 'name']

class CustomUserSerializer(serializers.ModelSerializer):
    """
    Currently unused in preference of the below.
    """
    email = serializers.EmailField(
        required=True
    )
    username = serializers.CharField()
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ('email', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)  # as long as the fields are the same, we can just use this
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'code', 'price', 'name_pl', 'name_en', 'product_description_pl', 
        'product_description_en', 'category_id', 'recommended', ]

class RelatedProductJunctionSerializer(serializers.ModelSerializer):
    class Meta:
        model = RelatedProductJunction
        fields = ['id', 'related']


class ProductPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductPhoto
        fields = ['id', 'product_id', 'main_photo', 'url']

class TextBoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextBox
        fields = ['id', 'name_pl', 'name_en', 'product_id', 'is_required', 'max_length']

class ComboBoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComboBox
        fields = ['id', 'name_pl', 'name_en', 'product_id', 'is_required']

class CalendarSerializer(serializers.ModelSerializer):
    model = Calendar
    fields = ['id', 'name_pl', 'name_en', 'is_required', 'product_id']

class ComboBoxValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComboBoxValue
        fields = ['id', 'text_en', 'text_pl', 'combo_box_id']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name_pl', 'name_en']

class CarouselSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carousel
        fields = ['id', 'enabled']

class CarouselPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarouselPhoto
        fields = ['id', 'url']      
