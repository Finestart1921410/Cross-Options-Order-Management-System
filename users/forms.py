from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm



class RegisterForm(UserCreationForm):
    # fields we want to include and customize in our form
    
    first_name = forms.CharField(max_length=100,
                                 required=True,
                                 widget=forms.TextInput(attrs={'placeholder': 'User ID',
                                                               'class': 'form-control',
                                                               }))
    last_name = forms.CharField(max_length=100,
                                required=True,
                                widget=forms.TextInput(attrs={'placeholder': 'Age',
                                                              'class': 'form-control',
                                                              }))
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Username',
                                                             'class': 'form-control',
                                                             }))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'placeholder': 'Email',
                                                           'class': 'form-control',
                                                           }))
    password1 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                  'class': 'form-control',
                                                                  'data-toggle': 'password',
                                                                  'id': 'password',
                                                                  }))
    password2 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password',
                                                                  'class': 'form-control',
                                                                  'data-toggle': 'password',
                                                                  'id': 'password',
                                                                  }))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Username',
                                                             'class': 'form-control',
                                                             }))
    password = forms.CharField(max_length=50,
                               required=True,
                               widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                 'class': 'form-control',
                                                                 'data-toggle': 'password',
                                                                 'id': 'password',
                                                                 'name': 'password',
                                                                 }))
    remember_me = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = ['username', 'password', 'remember_me']



from django import forms  
from users.models import Employee  
class EmployeeForm(forms.ModelForm):  
    class Meta:  
        model = Employee  
        fields = ['trade', 'date', 'shares', 'symbols', 'buysell', 'payment', 'userid', 'age', 'username', 'email'] 
        widgets = { 'trade': forms.TextInput(attrs={ 'class': 'form-control' }), 
                   'date': forms.TextInput(attrs={ 'class': 'form-control' }), 
                   'shares': forms.TextInput(attrs={ 'class': 'form-control' }), 
                   'symbols': forms.TextInput(attrs={ 'class': 'form-control' }), 
                   'buysell': forms.TextInput(attrs={ 'class': 'form-control' }), 
                   'payment': forms.TextInput(attrs={ 'class': 'form-control' }), 
                   'userid': forms.TextInput(attrs={ 'class': 'form-control' }), 
                                      'age': forms.TextInput(attrs={ 'class': 'form-control' }), 

                   'username': forms.TextInput(attrs={ 'class': 'form-control' }), 
                   'email': forms.TextInput(attrs={ 'class': 'form-control' }), 

            
      }
        



