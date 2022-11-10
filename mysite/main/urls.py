from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='main_home'),
	path('about/', views.about, name='main_about'),
	path('posts/', views.post_list, name='post_list'),
	path('posts/<slug:post>/', views.post_detail, name='post_detail'),
]