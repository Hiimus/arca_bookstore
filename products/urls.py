from django.urls import path
from . import views 


urlpatterns = [
    path('', views.all_books, name='products'),
    path('arts/', views.all_arts_and_crafts, name='artsandcraft'),
    path('games/', views.all_games, name='games'),
]
