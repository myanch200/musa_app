from django.shortcuts import render,get_object_or_404,redirect
from .models import Poem
from .forms import RegisterUserForm
from django.contrib import messages
# Create your views here.
def home(request):
    poems =Poem.objects.all().order_by('-date_created')[:6]
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

def login(request):
    return render(request,'accounts/login.html')