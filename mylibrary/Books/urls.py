from django.urls import path, include
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [

    path('edb/<int:id>/', login_required(views.EditBook.as_view(),login_url='/login/'), name='edit'),
    path('del/<int:id>/', login_required(views.DeleteBook.as_view(),login_url='/login/'), name='delete'),

    path('add/', login_required(views.AddBook.as_view(),login_url='/login/'), name='add'),
]