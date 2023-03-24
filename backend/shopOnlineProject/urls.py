from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import settings

from store.views.signup import Signup
from store.views.login import Login, logout
from store.views.basket import Basket
from store.views.order import OrderView
from store.views.checkout import СheckOut
from user.views import UserUpdateView
from store.middlewares.auth import auth_middleware

urlpatterns = [
    path('admin/', admin.site.urls),
    # Ауентификация
    # path('logout/', views.logoutuser, name='logout'), # выход
    path('', include('store.urls'), name='main-page'),
    path('signup/', Signup.as_view(), name='signup'),  # регистрация
    #path('login/', Login.as_view(), name='login'), # вход
    path('logout/', logout, name='logout'),  # выход
    path('basket/', Basket.as_view(), name='basket'),
    path('orders/', OrderView.as_view(), name='orders'),
    path('checkout/', СheckOut.as_view(), name='checkout'),
    path('user/<int:pk>', UserUpdateView.as_view(), name='main-page'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('user.urls'))


]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
