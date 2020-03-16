from django.urls import path
from . import views

urlpatterns = [
    path('edit/', views.edit_view),
    path('upload/', views.upload_view, name='upload'),
    path('oversight/', views.oversight_view, name='oversight'),
]