from django.urls import path, include
from . import views

urlpatterns = [

    path('abs/', views.AllBooks.as_view(), name='all_books'),
]