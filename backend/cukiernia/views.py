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
from .models import Category, Carousel, CarouselPhoto, Product

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
            data = Product.objects.filter(category_id=request.GET.get('category',''))
            serializer = ProductSerializer(data, many=True)
            return JsonResponse(serializer.data, safe=False)
        elif request.GET.get('recommend','') != "":
            data = Product.objects.filter(recommended=request.GET.get('recommend',''))
            serializer = ProductSerializer(data, many=True)
            return JsonResponse(serializer.data, safe=False)
        else:
            data = Product.objects.all()
            serializer = ProductSerializer(data, many=True)
            return JsonResponse(serializer.data, safe=False)
    

@api_view(['GET',])
@permission_classes([AllowAny])
def product(request, pk):
    try:
        data = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ProductSerializer(data)
        return JsonResponse(serializer.data)
