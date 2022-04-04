from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('create/', views.create, name='create'),
    path('comment/<int:id>/', views.comment, name='comment'),
    path('like/', views.like, name="like"),
    path('profile/<int:id>/', views.profile, name="profile"),
    path('edit/<int:id>/', views.edit, name="edit"),
    path('register/', views.register, name='register'),
    path('single/<int:id>/', views.single, name='single'),
]