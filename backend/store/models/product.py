from django.db import models
from .category import Category
from django.urls import reverse


class Product(models.Model):
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    name = models.CharField(verbose_name='Продукт', max_length=100)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Категория', default=1000)  # CASCADE
    price = models.PositiveIntegerField(verbose_name='Цена', default=0)
    description = models.CharField(verbose_name='Описание', max_length=200, blank=True)
    image = models.ImageField(verbose_name='Фото', upload_to='uploads/products/')

    def __str__(self):
        return self.name

    @staticmethod
    def get_products_by_id(list_id):
        return Product.objects.filter(pk__in=list_id)

    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_all_products_by_category_id(category_id):
        if category_id:
            return Product.objects.filter(category=category_id)
        else:
            return Product.get_all_products()

    # @staticmethod
    # def get_absolute_url():
    #     return reverse('post',kwargs={
    #         'post_id':id
    #     })
