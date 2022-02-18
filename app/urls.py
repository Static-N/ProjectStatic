from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('home/search',views.gen),
    path('<str:pk>/', views.WSmain),
    path('WSinfo/<str:pk>/',views.WSinfo)
    
]