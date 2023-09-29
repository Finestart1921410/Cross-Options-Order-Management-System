from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views import View
from django.contrib.auth.decorators import login_required

from .forms import RegisterForm, LoginForm

def home(request):
    
    return render(request, 'users/home.html')


class RegisterView(View):
    form_class = RegisterForm
    initial = {'key': 'value'}
    template_name = 'users/register.html'

    def dispatch(self, request, *args, **kwargs):
        # will redirect to the home page if a user tries to access the register page while logged in
        if request.user.is_authenticated:
            return redirect(to='/')

        # else process dispatch as it otherwise normally would
        return super(RegisterView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')

            return redirect(to='login')

        return render(request, self.template_name, {'form': form})


# Class based view that extends from the built in login view to add a remember me functionality
class CustomLoginView(LoginView):
    form_class = LoginForm

    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')

        if not remember_me:
            # set session expiry to 0 seconds. So it will automatically close the session after the browser is closed.
            self.request.session.set_expiry(0)

            # Set session as modified to force data updates/cookie to be saved.
            self.request.session.modified = True

        # else browser session will be as long as the session cookie time "SESSION_COOKIE_AGE" defined in settings.py
        return super(CustomLoginView, self).form_valid(form)
    


from users.forms import EmployeeForm  
from users.models import Employee  


 
# Create your views here.  
def addnew(request):  
    if request.method == "POST":  
        form = EmployeeForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/')  
            except:  
                pass
    else:  
        form = EmployeeForm()  
    return render(request,'users/addnew.html',{'form':form})  

 


def home(request):  
    employees = Employee.objects.all()   
    return render(request,"users/home.html",{'employees':employees})  
 
def edit(request, id):  
    employee = Employee.objects.get(id=id)  
    return render(request,'users/edit.html', {'employee':employee})  
 
def update(request, id):  
    employee = Employee.objects.get(id=id)  
    form = EmployeeForm(request.POST, instance = employee)  
    if form.is_valid():  
        form.save()  
        return redirect("show")  
    return render(request, 'users/edit.html', {'employee': employee})  
     
def destroy(request, id):  
    employee = Employee.objects.get(id=id)  
    employee.delete()  
    return redirect("show")  

from django.contrib import messages

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        age = request.POST.get('age')

        password = request.POST.get('password')

        if username == 'admin123' and password == 'admin123' and age == 'admin123' :
            # Authentication successful
            request.session['is_authenticated'] = True  # Set a session variable
            return redirect('show')
        else:
            messages.error(request, 'Invalid credentials. Please try again.')
    return render(request, 'users/adminlogin.html')

def show(request):
    if not request.session.get('is_authenticated'):
        return redirect('adminlogin')  # Redirect to login page if not authenticated

    # Assuming you have some logic to retrieve employee data
    employees = Employee.objects.all()
    return render(request, 'users/show.html', {'employees': employees})


