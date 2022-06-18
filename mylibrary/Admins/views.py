from django.views import View, generic
from django.contrib.auth import views as auth_views
from django.http.response import Http404, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from Admins.forms import AdminSignUpForm, LoginForm
from django.urls import reverse_lazy



# Create your views here.

#==============================================================================#
class Test(View):
    
    def get(self,request):
        print('I am testing')
        return render(request,'base.html',locals())
#==============================================================================#

#==============================================================================#
class Home(View):
    def get(self,request):
        if request.GET:
            print('i am getting')
            print(request.GET,)
        else:
            return render(request,'welcome.html',locals())
        return render(request,'welcome.html',locals())
#==============================================================================#   

#==============================================================================#
def view_login(request):

    title='Please login to continue'
    domain_name = 'TFGridlex'

    try:
        if request.user.is_active:
            return redirect('/')
    except Exception as e:
        pass

    if request.method=='POST':
        username = request.POST.get('username', None)
        #print('username',username)
        username = username.lower()
        passwd = request.POST.get('password', None)

        user = authenticate(username=username, password=passwd)
        
        # user = authenticate(username, password=passwd)
        if user and user.is_active:
            login(request, user)
            userid = request.user.id
            eid= user.id

            if request.POST.get("next", None):
                redirect_to = request.POST.get("next", None)
            else:
                redirect_to = '/home/'

            return redirect(redirect_to)

        else:
            error_msg = "Your User ID & Password Combination is Incorrect"


    next = request.GET.get('next', '')

    return render(request, 'login.html', locals())
# #==============================================================================#

#==============================================================================#
def view_logout(request):
    logout(request)
    return redirect('/login/')
#==============================================================================#

#==============================================================================#
class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'login.html'
    success_url = reverse_lazy('library_home')
#==============================================================================#

#==============================================================================#
class RegisterView(generic.CreateView):
    form_class = AdminSignUpForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')