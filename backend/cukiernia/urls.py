from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('register/', views.CustomUserCreate.as_view(), name="create_user"),
    path('login/', views.CustomObtainAuthToken.as_view()),
    path('categories/', views.categories_list),




]