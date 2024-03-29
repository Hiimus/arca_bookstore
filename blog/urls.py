from django.urls import path
from . import views


urlpatterns = [
    path('', views.view_blog, name='view_blog'),
    path('blogpost/<int:blog_id>/', views.blog_info, name='blog_info'),
    path('post/', views.add_post, name='add_post'),
    path('comment/<int:blog_id>/', views.add_comment, name='add_comment'),
    path('comment/<int:comment_id>/delete/',
         views.delete_comment, name='delete_comment'),
    path('blogpost/<int:blog_id>/delete/',
         views.delete_post, name='delete_post'),
    path('blogpost/<int:blog_id>/edit/', views.edit_post, name='edit_post'),
]
