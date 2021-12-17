from django.urls import path
from . import views 


urlpatterns = [
    path('', views.view_blog, name='view_blog'),
    path('post/', views.add_post, name='add_post'),
    path('comment/', views.add_comment, name='add_comment'),
]
