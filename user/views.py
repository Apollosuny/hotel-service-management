from django.shortcuts import render, redirect, get_object_or_404
from .forms import * 
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required, user_passes_test

# Create your views here.
def loginUser(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.role == 'USER':
                login(request, user)
                return redirect('home')
            elif user.is_staff == True and user.role == 'STAFF':
                login(request, user)
                # messages.success(request, 'Đăng nhập thành công')
                return redirect('dashboard')
            # elif user.is_superuser and user.is_staff:
            #     login(request, user)
            #     # messages.success(request, 'Đăng nhập thành công')
            #     return redirect('developer_dashboard')
            else:
                return redirect('login')
        else:
            # Return an 'invalid login' error message.
            return redirect('login')
    return render(request, 'user/login.html')

def registerCustomer(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    form = UserRegistrationForm()
    return render(request, 'user/register.html', { 'form': form })

def registerStaff(request):
    if request.method == 'POST':
        form = StaffRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    form = StaffRegistrationForm()
    return render(request, 'user/staff-register.html', { 'form': form })

def logoutUser(request):
    logout(request)
    return redirect('home')

@login_required(login_url='login')
def profile(request):
    user = get_object_or_404(Customer, user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            # Update the instance with form data
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.phone = form.cleaned_data['phone']
            user.national_id = form.cleaned_data['national_id']
            user.save()
            return redirect('profile')
    else:
        form = ProfileForm(initial={ 'first_name': user.first_name, 'last_name': user.last_name, 'phone': user.phone, 'national_id': user.national_id })
    return render(request, 'user/profile.html', { 'form': form })