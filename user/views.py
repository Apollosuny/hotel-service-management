from django.shortcuts import render, redirect
from .forms import * 
from django.contrib.auth import authenticate, login, logout, get_user_model

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
            # elif user.is_staff == True and user.is_superuser == False:
            #     login(request, user)
            #     # messages.success(request, 'Đăng nhập thành công')
            #     return redirect('admin-page')
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