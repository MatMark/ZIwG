from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('register/', views.CustomUserCreate.as_view(), name="create_user"),
    path('login/', views.CustomObtainAuthToken.as_view()),
    path('categories/', views.categories_list),
    path('carousel/', views.carousel),
    path('products/', views.products_list),
    path('product/<int:pk>/', views.product),
    path('orders/', views.orders_list),
    path('order/<int:pk>/', views.order),
    path('decorations/', views.decorations_list),



]