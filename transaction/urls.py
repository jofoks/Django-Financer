from django.urls import path
from . import views

urlpatterns = [
    path('detail/', views.detail_view),
    path('edit/', views.edit_view),
    path('test/', views.home_widget),
]