from django.urls import path
from . import views

urlpatterns = [
    path('create_shoe/', views.create_shoe, name='create_shoe'),
    path('delete_shoe/<int:shoe_id>/', views.delete_shoe, name='delete_shoe'),
    path('search_shoe/', views.search_shoe, name='search_shoe'),
]
