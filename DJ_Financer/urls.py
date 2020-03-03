from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.contrib.auth import views as auth_view
from accounts import views as account_views

urlpatterns = [
    path('', account_views.home_view, name='home'),
    path('admin/', admin.site.urls),
    path('login/', auth_view.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('register/', account_views.register_view, name='register'),
    path('home/', account_views.home_view, name='home'),
]
