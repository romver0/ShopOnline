from django.db import models
# from django.contrib.auth.models import User


class InfoUser(models.Model):
    class Meta:
        verbose_name = 'Пользователя'
        verbose_name_plural = 'Пользователи'

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    password = models.CharField(max_length=500)
    phone = models.CharField(max_length=15)
    email = models.EmailField()

    # user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def register(self):
        self.save()

    @staticmethod
    def get_infoUser_by_email(email):
        try:
            return InfoUser.objects.get(email=email)
        except:
            return False

    def isExists(self):
        if InfoUser.objects.filter(email=self.email):
            return True
        return False
