import datetime

from django.db import models

from store.models import Product, InfoUser


class Order(models.Model):
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    customer = models.ForeignKey(InfoUser, on_delete=models.CASCADE, verbose_name='Пользователь')
    amount = models.PositiveIntegerField(default=1, verbose_name='Кол-во')
    price = models.PositiveIntegerField(verbose_name='Цена')
    address = models.CharField(max_length=50, default='', blank=True, verbose_name='Адрес')
    phone = models.CharField(max_length=50, default='', blank=True, verbose_name='Телефон')
    date = models.DateTimeField(default=datetime.datetime.today)
    order_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата заказа')
    update_date = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    status = models.BooleanField(default=False)

    def __str__(self):
        return f' Номер заказа - {self.id}'

    def register(self):
        self.save()

    @staticmethod
    def get_basket_by_customer(customer_id):
        return Order.objects.filter(customer=customer_id).order_by('-order_date')
