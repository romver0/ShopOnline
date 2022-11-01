from django.contrib import admin
from .models.product import Product
from .models.category import Category
from .models.order import Order
from .models.infoUser import InfoUser


class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']


class AdminCategory(admin.ModelAdmin):
    list_display = ['name']


class AdminOrder(admin.ModelAdmin):
    list_display = ['customer', 'product', 'amount', 'price', 'address', 'order_date']
    search_fields = ('customer', 'address', 'order_date')


admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategory)
admin.site.register(Order, AdminOrder)
admin.site.register(InfoUser)
