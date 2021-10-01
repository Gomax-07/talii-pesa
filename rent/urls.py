from django.urls import path, include
from . import views
from .views import *

urlpatterns = [
    path('index/', views.index, name='index'),
    path('', views.landing, name='landing'),

# House_paths
    path('house/', views.HouseListView.as_view(), name='house'),
    path('house/<int:pk>/', views.HouseDetailView.as_view(), name='house-detail'),
    path('house/create/', house_create, name='house_create'),


#Tenants_paths
     path('house/tenant_create/', tenant_create, name='tenant_create'),
     path('house/tenant/', views.TenantListView.as_view(), name='tenant'),
]

