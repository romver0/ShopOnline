from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from .views.home import Home, store, product_profile


urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('store/', store, name='store'),
    path('product/<slug:product_id>/', product_profile, name='product profile'),
]
