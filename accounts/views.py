from django.shortcuts import render,get_object_or_404,redirect
from .models import Poem
from django.contrib.auth.forms import AuthenticationForm

from .forms import RegisterUserForm ,CreatePoemForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
# Create your views here.
def home(request):
    poems =Poem.objects.all().order_by('-date_created')[:10]
    context = {
        'poems': poems,
    }
    return render(request,'accounts/index.html',context)


def poem_details(request, pk):
    poem = get_object_or_404(Poem,id=pk)
    context = {'poem':poem}
    return render(request,'accounts/poem_details.html',context)

def register(request):
    form = RegisterUserForm()
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')
        else:
            messages.error(request, 'invalid, please try again')
    context = {'form':form}
    return render(request,'accounts/register.html',context)

def user_login(request):
    
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(request = request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username, password =password)
            if user is not None:
                login(request, user)
                messages.success(request,f'{user.username} successfully logged in')
                return redirect('/')

            else:
                messages.error(request,"Wrong username or password")
    context = {'form':form}
       
    return render(request,'accounts/login.html',context)


def user_logout(request):
    logout(request)
    messages.success(request, 'Logged out')
    return redirect('accounts:home')

def write_poem(request,pk):
    user = User.objects.get(id=pk)
    form = CreatePoemForm()
    if request.method == 'POST':
        form = CreatePoemForm(request.POST)
        if form.is_valid():
            poem = form.save(commit=False)
            poem.author = user
            poem.save()
            return redirect('accounts:home')
    context = {'form':form}

    return render(request,'accounts/write_poem.html',context)

