from django.urls import path
from . import views

urlpatterns = [
    path('books/create/', views.create_book, name='create_book'),
    path('books/delete/<int:book_id>/', views.remove_book, name='delete_book'),
    path('books/search/', views.book_search, name='book_search'),
    path('books/get_all_books/', views.get_books, name='get_books'),
]
