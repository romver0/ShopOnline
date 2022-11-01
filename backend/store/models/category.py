from django.db import models


class Category(models.Model):
    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'

    name = models.CharField(max_length=50, db_index=True, verbose_name='Категория')

    def __str__(self):
        return self.name

    @staticmethod
    def get_all_categories():
        return Category.objects.all()
