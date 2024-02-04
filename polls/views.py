from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
# Create your views here.

#homepage
def home(request):
   return render(request, 'polls/index.html')


#register a user
def user_register(request):
   form = CreateUserForm()
   if request.method == 'POST':
      form = CreateUserForm(request.POST)
      if form.is_valid():
         form.save()
   
   context = {'form': form}
   return render(request, 'polls/register.html', context = context)


#login form
def user_login(request):
   form = LoginForm()
   if(request.method == 'POST'):
      form = LoginForm(request.POST)
      if form.is_valid():
         username = request.POST.get('username')
         password = request.POST.get('password')
         user = authenticate(request, username, password)
         
      if user is not None:
         auth.login(request, user)
         return redirect('login')
      
   context = {'form': form}
   return render(request, 'polls/my-login.html', context = context)   
   
   
#logout User
def user_logout(request):
   auth.logout(request)
   return redirect('/login')

#Dashboard
