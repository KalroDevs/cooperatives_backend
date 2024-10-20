from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from cooperatives.models import *

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('role_redirect')
        else:
            return render(request, 'index.html', {'error': 'Invalid credentials'})
    return render(request, 'index.html')

@login_required
def role_redirect(request):
    if request.user.role == 'admin':
        dashboards = Dashboards.objects.all() 
        return render(request, 'home/admin_dashboard.html', {'dashboards': dashboards})
    elif request.user.role == 'national':
        dashboards = Dashboards.objects.all() 
        return render(request, 'home/national_dashboard.html', {'dashboards': dashboards})
    elif request.user.role == 'county':
        dashboards = Dashboards.objects.filter(role='county') 
        return render(request, 'home/county_dashboard.html', {'dashboards': dashboards})
    elif request.user.role == 'fa':
        dashboards = Dashboards.objects.filter(role='fa')
        return render(request, 'home/fa_dashboard.html', {'dashboards': dashboards})
    elif request.user.role == 'sp':
        dashboards = Dashboards.objects.filter(role='sp')
        return render(request, 'home/sp_dashboard.html', {'dashboards': dashboards})
    else:
        return redirect('login')



from .forms import CustomUserCreationForm

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the user to the database
            login(request, user)  # Log in the user after registration
            return redirect('role_redirect')  # Redirect based on role
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})



@login_required
def admin_dashboard(request):
    if request.user.role == 'admin':        
        dashboards = Dashboards.objects.all() 
        return render(request, 'home/admin_dashboard.html', {'dashboards': dashboards})
    else:
        return redirect('login')
    

@login_required
def national_dashboard(request):
    if request.user.role == 'national':
        dashboards = Dashboards.objects.all() 
        return render(request, 'home/national_dashboard.html', {'dashboards': dashboards})
    else:
        return redirect('login')
    

@login_required
def county_dashboard(request):
    if request.user.role == 'county':
        dashboards = Dashboards.objects.filter(role='county') 
        return render(request, 'home/county_dashboard.html', {'dashboards': dashboards})
    else:
        return redirect('login')

@login_required
def fa_dashboard(request):
    if request.user.role == 'fa':
        dashboards = Dashboards.objects.filter(role='fa')
        return render(request, 'home/fa_dashboard.html', {'dashboards': dashboards})
    else:
        return redirect('login')
    
@login_required
def sp_dashboard(request):
    if request.user.role == 'sp':
        dashboards = Dashboards.objects.filter(role='sp')
        return render(request, 'home/sp_dashboard.html', {'dashboards': dashboards})
    else:
        return redirect('login')


from django.views.generic import ListView
class SaccoRegistry(ListView):
    model = Cooperative
    template_name = 'home/sacco_registry.html'  # Specify your template here
    context_object_name = 'cooperatives'  # The context name that will be used in the template
    paginate_by = 10



