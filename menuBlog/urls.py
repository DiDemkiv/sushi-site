from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu_page, name='menu_page'),
    path('dish/<str:name>/', views.dish_detail, name='dish_detail'),
]