from django.db import models


class TestModel(models.Model):
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=50, blank=True)
