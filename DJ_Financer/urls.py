from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from accounts import views as account_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', account_views.login_view, name='login'),
    path('register/', account_views.register_view, name='register'),
]
