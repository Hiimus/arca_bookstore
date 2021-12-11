from django.urls import path
from . import views 


urlpatterns = [
    path('', views.all_books, name='products'),
    path('search/', views.search, name='search'),
    path('arts/', views.all_arts_and_crafts, name='artsandcrafts'),
    path('arts/<int:product_id>/', views.product_detail, name='product_detail'),
    path('books/', views.all_books, name='products'),
    path('books/<int:product_id>/', views.product_detail, name='product_detail'),
    path('games/', views.all_games, name='games'),
    path('games/<int:product_id>/', views.product_detail, name='product_detail'),
    path('add/', views.add_product, name='add_product'),
]

