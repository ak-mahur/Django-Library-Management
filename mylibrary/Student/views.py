
from django.views import View
from django.http.response import Http404, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

from Books.models import *

# Create your views here.

#==============================================================================#
class AllBooks(View):
    def get(self,request):
        title='All Books'
        book_obj=BookList.objects.exclude(deleted_flag=True).values('id','title','author','published_date','genre').order_by('title')

        head=['No','Title of Book', 'Name of Author', 'Date Published', 'Genre']
        return render(request,'all_books.html',locals())

