from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('service/<int:pk>/', views.service_detail, name='service_detail'),
    path('agendar/', views.book_appointment, name='book_appointment'),
]
