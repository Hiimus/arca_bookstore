from django.urls import path
from . import views 


urlpatterns = [
    path('faq/', views.view_faq, name='view_faq'),
    path('policies/', views.view_policies, name='view_policies'),
    path('contact/', views.view_contact, name='view_contact'),
]
