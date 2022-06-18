from django.urls import path, include
from . import views

urlpatterns = [

    path('',views.Home.as_view(), name='library_home'),
    path('home/', views.Home.as_view(), name='library_home'),
    path('logout/', views.view_logout, name='view_logout'),
    path('login/', views.LoginView.as_view(), name='login'),
    # path('login/', views.view_login, name='login'),
    path('signup/',views.RegisterView.as_view(), name='signup'),
]
