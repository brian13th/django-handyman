from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, UserPropertyForm, ProfileForm
from django.contrib.auth.decorators import login_required
from .models import Property
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm



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
@login_required
def profile(request):
    if request.method == 'POST':
        form_prof = ProfileForm(request.POST, instance=request.user)
        form_prop = UserPropertyForm(request.POST, instance=request.user.property)

        if form_prof.is_valid() and form_prop.is_valid():
            form_prof.save()
            form_prop.save()
            messages.success(request, f'You have successfully updated your profile!')
            return redirect('users-profile')
    else:
        form_prof = ProfileForm(instance=request.user)
        form_prop = UserPropertyForm(instance=request.user.property)
    return render(request, 'users/profile.html', {'form_prop': form_prop, 'form_prof':form_prof})
