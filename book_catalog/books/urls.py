from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),  
    path('book/create/', views.book_create, name='book_create'),  
    path('book/<int:pk>/update/', views.book_update, name='book_update'), 
    path('book/<int:pk>/delete/', views.book_delete, name='book_delete'), 
]
