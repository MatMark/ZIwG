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
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from .serializers import UserSerializer, CustomUserSerializer, CategorySerializer, CarouselSerializer, ProductSerializer
from .models import Category, Carousel, CarouselPhoto, Product, ProductPhoto, TextBox, ComboBox, ComboBoxValue, RelatedProductJunction, Calendar

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
@permission_classes([])
def categories_list(request):
    if request.method == 'GET':
        data = Category.objects.all()
        serializer = CategorySerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)

@api_view(['GET',])
@authentication_classes([])
def carousel(request):
    if request.method == 'GET':
        data = Carousel.objects.all()
        result = {'enabled':data[0].enabled,}
        if data[0].enabled:
            photos = list(CarouselPhoto.objects.all().values('url'))
            result['photos'] = photos
        return JsonResponse(result, safe=False)

@api_view(['GET',])
@permission_classes([])
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
        return JsonResponse(data, safe=False)

@api_view(['GET',])
@permission_classes([])
def product(request, pk):
    try:
        data = list(Product.objects.filter(pk=pk).values())[0]
    except Product.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        photos = list(ProductPhoto.objects.filter(product_id=pk).values('url'))
        combo_boxes = list(ComboBox.objects.filter(product_id=pk).values('id', 'name_pl', 'name_en', 'is_required'))
        related_products_ids = list(RelatedProductJunction.objects.filter().values('related_second'))
        related_products = []
        for key in related_products_ids:
            product = list(Product.objects.filter(pk=key['related_second']).values())[0]
            photo = list(ProductPhoto.objects.filter(product_id=product['id']).filter(main_photo=True).values('url'))
            if len(photo)>0:
                product['photo']=photo[0]['url']
            else:
                product['photo'] = ''
            related_products.append(product)
        data['related_products'] = related_products
        for combo_box in combo_boxes:
            combo_box['values'] = list(ComboBoxValue.objects.filter(combo_box_id=combo_box['id']).values('text_pl', 'text_en'))
        data['combo_boxes'] = combo_boxes
        data['text_boxes'] = list(TextBox.objects.filter(product_id=pk).values('id', 'name_pl', 'name_en','is_required'))
        data['calendars'] = list(Calendar.objects.filter(product_id=pk).values('id', 'name_pl', 'name_en','is_required'))
        data['photos'] = photos
        return JsonResponse(data)
