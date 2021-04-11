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
from .serializers import UserSerializer, CustomUserSerializer, CategorySerializer
from .models import Category

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

@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def categories_list(request):
    if request.method == 'GET':
        data = Category.objects.all()
        serializer = CategorySerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CategorySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)