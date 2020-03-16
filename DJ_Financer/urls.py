from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.contrib.auth import views as auth_view
from accounts import views as account_views
from transaction import views as trans_views
from accounts.forms import SignInFrom, RegisterForm


urlpatterns = [
    path('', account_views.home_view, name='home'),
    path('admin/', admin.site.urls),
    path('home/', account_views.home_view, name='home'),
    path('transactions/', include(('transaction.urls', 'transactions'),namespace='transactions')),
    # path('account/', include('accounts.urls')),
    path('login/', auth_view.LoginView.as_view(authentication_form=SignInFrom, template_name='accounts/login.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='accounts/logout.html'), kwargs= {'placeholder':'Yeet'}, name='logout'),
    path('register/', account_views.register_view, name='register'),
    path('account/', account_views.initial_view, name='initial'),
]