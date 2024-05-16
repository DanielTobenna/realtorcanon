from django.urls import path

from . import views

urlpatterns=[
	path('', views.home, name="home"),
	path('about/', views.about, name="about"),
	path('contact/', views.contact, name="contact"),
	path('suscribe/', views.suscribe, name="suscribe"),
	path('property/', views.property, name="property"),
	path('propertyInfo/<str:pk>/', views.propertyInfo, name="propertyInfo"),
	path('propertyAgent/<str:pk>/', views.propertyAgent, name="propertyAgent"),
]