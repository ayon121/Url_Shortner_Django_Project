from django.urls import path 
from . import views

urlpatterns = [
    path('' , views.home , name= 'home'),
    path('<slug:key>/', views.route_to_url )
]

