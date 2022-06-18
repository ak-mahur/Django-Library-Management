
from .models import *
from django.views import View
from django.http.response import Http404, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

# Create your views here.

class EditBook(View):
    def get(self, request, id):
        title='Update book'

        obj=BookList.objects.filter(id=id).values('title','author','published_date','genre')
        data=obj[0]

        return render(request,'edit.html',locals())
    
    def post(self,request, id):
        d={}
        d['title']=request.POST.get('title','')
        d['author']=request.POST.get('author','')
        d['genre']=request.POST.get('genre','')
        d['published_date']=request.POST.get('pub_date',None)
        BookList.objects.filter(id=id).update(**d)
        return redirect('/abs/')

class DeleteBook(View):
    def get(self, request, id):
        

        obj=BookList.objects.filter(id=id).update(deleted_flag=True)
        # data=obj[0]

        return redirect('/abs/')


class AddBook(View):
    def get(self, request):
        title='Add Book'

        return render(request,'add.html',locals())

    def post(self,request):
        d={}
        d['title']=request.POST.get('title','')
        d['author']=request.POST.get('author','')
        d['genre']=request.POST.get('genre','')
        d['published_date']=request.POST.get('pub_date',None) 
        d['added_by']=AdminUser.objects.get(id=request.user.id) 
        BookList.objects.create(**d)
        return redirect('/abs/')

