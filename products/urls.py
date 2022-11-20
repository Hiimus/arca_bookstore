from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_products, name='all_products'),
    path('search/', views.search, name='search'),
    path('arts/', views.all_arts_and_crafts, name='artsandcrafts'),
    path(
        'arts/<int:product_id>/', views.product_detail, name='product_detail'),
    path('books/', views.all_books, name='products'),
    path(
        'books/<int:product_id>/', views.product_detail, name='product_detail'
        ),
    path('games/', views.all_games, name='games'),
    path(
        'games/<int:product_id>/', views.product_detail, name='product_detail'
        ),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path(
        'delete/<int:product_id>/', views.delete_product, name='delete_product'
        ),
    path('review/<int:product_id>/', views.add_review, name='add_review'),
    # path(
    #     'deleterev/<int:review_id>/', views.delete_review, name='delete_review'
    #     ),
    path(
    'deleterev/<int:review_id>/', views.delete_review_author, name='delete_review_author'
    ),
]
