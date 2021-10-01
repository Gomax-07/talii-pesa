from django.urls import path, include
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('house/', views.HouseListView.as_view(), name='house'),
    path('house/<int:pk>', views.HouseDetailView.as_view(), name='house-detail'),
    path('', views.landing, name='landing')
]

