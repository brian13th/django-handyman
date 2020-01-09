from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, UserPropertyForm, ProfileForm
from .models import Property
from django.contrib.auth.models import User
from django.contrib import messages



def index(request):
    return render(request, 'users/index.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        form_p = UserPropertyForm(request.POST)

        if form.is_valid() and form_p.is_valid():
            form.save()
            status = form_p.cleaned_data.get('status')
            username = form.cleaned_data.get('username')
            Property.objects.create(status=status, user=User.objects.get(username=username))
            messages.success(request, f'You have successfully created an account as {username}! You can now login!')
            return redirect('users-login')

    else:
        form = UserRegistrationForm()
        form_p = UserPropertyForm()
    return render(request, 'users/register.html', {'form':form, 'form_p':form_p})
