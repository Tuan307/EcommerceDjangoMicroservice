from django.urls import path
from . import views
from .all_views import  cart_views, order_views, user_views, products_views

urlpatterns = [

    # User
    path('register/', user_views.register, name='register'),
    path('get_users/', user_views.get_users, name='get_users'),

    #Books
    path('add_book/', products_views.register_book, name='register_book'),
    path('get_all_books/', products_views.get_books, name='get_books'),
    path('book/delete/<int:book_id>/', products_views.delete_book, name='delete_book'),
    path('search_books/', products_views.book_search, name='book_search'),

    # Products
    path('add_shoes/', products_views.register_shoes, name='register_shoes'),
    path('add_clothes/', products_views.register_clothes, name='register_clothes'),

    # Cart
    path('add_product_to_cart/', cart_views.add_product_to_cart, name='add_product_to_cart'),
    path('remove_item_from_cart/', cart_views.remove_item_from_cart, name='remove_item_from_cart'),
    path('show_cart/', cart_views.show_cart, name='show_cart'),
    path('purchase/', cart_views.purchase, name='purchase'),

    # Order
    path('track_order/', order_views.track_order, name='track_order'),
    path('update_order/', order_views.update_order, name='update_order'),
]