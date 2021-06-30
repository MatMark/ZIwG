from django.urls import path
from rest_framework import viewsets
from rest_framework import status
from django.contrib.auth.models import User, Group
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from .serializers import UserSerializer, CustomUserSerializer, CategorySerializer, CarouselSerializer, ProductSerializer, OrderSerializer, DecorationSerializer
from .models import Category, Carousel, CarouselPhoto, Product, ProductPhoto, TextBox, ComboBox, ComboBoxValue
from .models import RelatedProductJunction, Calendar, Order, InstantRetail, OnDemandRetail, Decoration, Delivery
from datetime import date
from datetime import timedelta
import pandas as pd

# Create your views here.
class CustomUserCreate(APIView):

    permission_classes = (AllowAny,)
    authentication_classes = ()
    def post(self, request, format='json'):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            if User.objects.filter(email=request.data["email"]).exists():
                return Response(status=status.HTTP_400_BAD_REQUEST)
            user = serializer.save()
            if user:
                json = serializer.data
                token, created = Token.objects.get_or_create(user=user)
                json["token"] = token
                return Response(data={
            'token': token.key,
            'user_id': user.pk,
            'email': user.email}
        ,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(CustomObtainAuthToken, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        user = User.objects.get(pk=token.user_id)
        return Response({'token': token.key, 'id': token.user_id, 'is_admin': user.is_superuser})

@api_view(['GET',])
@permission_classes([AllowAny])
def categories_list(request):
    if request.method == 'GET':
        data = Category.objects.all()
        serializer = CategorySerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)

@api_view(['GET',])
@authentication_classes([AllowAny])
def carousel(request):
    if request.method == 'GET':
        data = Carousel.objects.all()
        result = {'enabled':data[0].enabled,}
        if data[0].enabled:
            photos = list(CarouselPhoto.objects.all().values('url'))
            result['photos'] = photos
        return JsonResponse(result, safe=False)

@api_view(['GET',])
@permission_classes([AllowAny])
def products_list(request):
    if request.method == 'GET':
        if request.GET.get('category','') != "":
            data = list(Product.objects.filter(category_id=request.GET.get('category','')).values())
            
        elif request.GET.get('recommend','') != "":
            data = list(Product.objects.filter(recommended=request.GET.get('recommend','')).values())
        else:
            data = list(Product.objects.all().values())
        for product in data:
            photo = list(ProductPhoto.objects.filter(product_id=product['id']).filter(main_photo=True).values('url'))
            if len(photo)>0:
                product['photo']=photo[0]['url']
            else:
                product['photo'] = ''
            retail = list(OnDemandRetail.objects.filter(product_id=product['id']).values())
            if len(retail) > 0:
                product['is_on_demand'] = True
                product['production_time'] = retail[0]['production_time']
            else:
                retail = list(InstantRetail.objects.filter(product_id=product['id']).values())
                if len(retail) > 0:
                    product['is_on_demand'] = False
                    product['quantity_available'] = retail[0]['quantity_available']
        return JsonResponse(data, safe=False)

@api_view(['GET',])
@permission_classes([AllowAny])
def product(request, pk):
    try:
        data = list(Product.objects.filter(pk=pk).values())[0]
    except Product.DoesNotExist:
        return HttpResponse(status=404)
    except IndexError:
        return HttpResponse(status=404)
        
    if request.method == 'GET':
        photos = list(ProductPhoto.objects.filter(product=pk).values('url'))
        combo_boxes = list(ComboBox.objects.filter(product=pk).values('id', 'name_pl', 'name_en', 'is_required'))
        related_products_ids = list(RelatedProductJunction.objects.filter(related_first=pk).values('related_second'))
        related_products = []
        for key in related_products_ids:
            product = list(Product.objects.filter(pk=key['related_second']).values())[0]
            photo = list(ProductPhoto.objects.filter(product=product['id']).filter(main_photo=True).values('url'))
            if len(photo)>0:
                product['photo']=photo[0]['url']
            else:
                product['photo'] = ''
            related_products.append(product)
        data['related_products'] = related_products
        for combo_box in combo_boxes:
            combo_box['values'] = list(ComboBoxValue.objects.filter(combo_box_id=combo_box['id']).values('text_pl', 'text_en', 'price_factor'))
        data['combo_boxes'] = combo_boxes
        data['text_boxes'] = list(TextBox.objects.filter(product=pk).values('id', 'name_pl', 'name_en','is_required', 'max_length'))
        data['calendars'] = list(Calendar.objects.filter(product=pk).values('id', 'name_pl', 'name_en','is_required'))
        data['photos'] = photos
        retail = list(OnDemandRetail.objects.filter(product=pk).values())
        if len(retail) > 0:
            data['is_on_demand'] = True
            data['production_time'] = retail[0]['production_time']
        else:
            retail = list(InstantRetail.objects.filter(product=pk).values())
            if len(retail) > 0:
                data['is_on_demand'] = False
                data['quantity_available'] = retail[0]['quantity_available']
        return JsonResponse(data)

@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def orders_list(request):
    if request.method == 'GET':
        if request.GET.get('user','') != "":
            data = list(Order.objects.filter(user=request.GET.get('user','')).values())
        else:
            data = list(Order.objects.all().values())
        for order in data:
            products_id = list(Order.objects.filter(pk=order['id']).values('products'))
            products = []
            for p_id in products_id:
                product = list(Product.objects.filter(pk=p_id['products']).values())[0]
                photo = list(ProductPhoto.objects.filter(product=p_id['products']).filter(main_photo=True).values('url'))
                if len(photo)>0:
                    product['photo']=photo[0]['url']
                else:
                    product['photo'] = ''
                products.append(product)
            order['products'] = products
        return JsonResponse(data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        decorations = data['decorations']
        data['price']=0
        on_demand = list(OnDemandRetail.objects.filter(product__in=data['products']).values())
        for p in on_demand:
            if date.today()+timedelta(days=p['production_time']) > pd.to_datetime(data['delivery_date']): 
                return HttpResponse(status=400)
        serializer = OrderSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            price = 0
            for dec in decorations:
                dec['order']=serializer.data['id']
                dec_serializer = DecorationSerializer(data=dec)
                if dec_serializer.is_valid():
                    dec_serializer.save()
                    price += dec['price']
            price += float(list(Delivery.objects.filter(pk=data['delivery']).values('price'))[0]['price'])
            products = list(Product.objects.filter(pk__in=data['products']).values('price'))
            for p in products:
                price+= (p['price'])
            serializer.data['price']=price
            Order.objects.filter(pk=serializer.data['id']).update(price=price)
            o = list(Order.objects.filter(pk=serializer.data['id']).values())[0]
            return JsonResponse(o, status=201)
        return JsonResponse(serializer.errors, status=400)
    return HttpResponse(status=400)



@api_view(['GET',])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def order(request, pk):
    try:
        data = list(Order.objects.filter(pk=pk).values())[0]
    except Product.DoesNotExist:
        return HttpResponse(status=404)
    products_id = list(Order.objects.filter(pk=pk).values('products'))
    products = []
    for p_id in products_id:
        product = list(Product.objects.filter(pk=p_id['products']).values())[0]
        photo = list(ProductPhoto.objects.filter(product=p_id['products']).filter(main_photo=True).values('url'))
        if len(photo)>0:
            product['photo']=photo[0]['url']
        else:
            product['photo'] = ''
        products.append(product)
    data['products'] = products
    return JsonResponse(data)

@api_view(['GET'])
@permission_classes([AllowAny])
def decorations_list(request):
    if request.method == 'GET':
        if request.GET.get('order','') != "":
            data = list(Decoration.objects.filter(order=request.GET.get('order','')).values())
        else:
            data = list(Decoration.objects.all().values())
        return JsonResponse(data, safe=False)
    return HttpResponse(status=400)

@api_view(['GET'])
@permission_classes([AllowAny])
def deliveries_list(request):
    data = list(Delivery.objects.all().values())
    return JsonResponse(data, safe=False)