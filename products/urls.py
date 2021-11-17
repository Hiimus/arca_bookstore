from django.urls import path
from . import views 


urlpatterns = [
    path('', views.all_arts_and_crafts, name='artsandcraft'),
    path('arts/', views.all_arts_and_crafts, name='artsandcraft'),
    path('arts/<product_id>', views.product_detail_arts, name='product_detail_arts'),
    path('books/', views.all_books, name='products'),
    path('books/<product_id>', views.product_detail, name='product_detail'),
    path('games/', views.all_games, name='games'),
    path('games/<product_id>', views.product_detail_games, name='product_detail_games'),
]

