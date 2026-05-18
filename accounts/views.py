from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from django.utils import timezone
from django.contrib import messages
from .models import SysUser, SysModule
from .forms import RegistrationForm

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful!")
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        emp_no = request.POST.get('employee_number')
        password = request.POST.get('password')
        try:
            user = SysUser.objects.get(employee_number=emp_no, is_active=True)
            if check_password(password, user.password_hash):
                request.session['user_id'] = user.user_id
                user.last_login = timezone.now()
                user.save()
                return redirect('dashboard')
            else:
                messages.error(request, "Invalid credentials")
        except SysUser.DoesNotExist:
            messages.error(request, "User not found")
        except Exception as e:
            messages.error(request, f"Database error: {e}")
    return render(request, 'login.html')


def dashboard(request):
    if 'user_id' not in request.session:
        return redirect('login')
    try:
        user = SysUser.objects.get(pk=request.session['user_id'])
        # Load top-level modules and prefetch submodules/components for navigation
        modules = SysModule.objects.filter(parent_module_id__isnull=True).prefetch_related(
            'submodules__components'
        )
        return render(request, 'dashboard.html', {
            'user': user,
            'modules': modules
        })
    except SysUser.DoesNotExist:
        messages.error(request, "Session expired. Please log in again.")
        return redirect('login')


def logout_view(request):
    request.session.flush()  # clears all session data
    messages.success(request, "You have been logged out.")
    return redirect('login')