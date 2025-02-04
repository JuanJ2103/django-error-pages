from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.core.validators import MinLengthValidator, MaxLengthValidator, MinValueValidator, MaxValueValidator

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'name', 'surname', 'control_number', 'age', 'tel', 'password1', 'password2']

        widgets = {
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Correo institucional',
                    'required': True,
                    'pattern': r'^[a-zA-Z0-9]+@utez\.edu\.mx$',
                    'title': 'Debe ingresar un correo válido UTEZ (@utez.edu.mx)',
                    'maxlength': 50,  
                }
            ),
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nombre',
                    'required': True,
                    'pattern': r'^[a-zA-Z]+(?: [a-zA-Z]+)*$',   
                    'title': 'Solo se permiten letras en el nombre',
                    'maxlength': 50,  
                }
            ),
            'surname': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Apellido',
                    'required': True,
                    'pattern': r'^[a-zA-ZáéíóúüñÁÉÍÓÚÜÑ]+(?: [a-zA-ZáéíóúüñÁÉÍÓÚÜÑ]+)*$',
                    'title': 'Solo se permiten letras en el apellido',
                    'maxlength': 50,  
                }
            ),
            'control_number': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Matricula',
                    'required': True,
                    'pattern': r'^[a-zA-Z0-9]{10,11}$',
                    'title': 'Solo se permiten matriculas solicitadas como 20223tn163',
                    'maxlength': 11,  
                }
            ),
            'age': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Edad',
                    'required': True,
                    'min': 15, 
                    'max': 60,       
                    'title': 'Debe ingresar una edad válida',
                }
            ),
            'tel': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Telefono',
                    'required': True,
                    'pattern': r'^\d{10}$',
                    'title': 'Debe ingresar un número de teléfono válido de 10 dígitos',
                    'maxlength': 10,  
                }
            ),
            'password1': forms.PasswordInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Contraseña',
                    'required': True,
                    'minlength': 8,  
                }
            ),
            'password2': forms.PasswordInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Confirmar Contraseña',
                    'required': True,
                    'minlength': 8,  
                }
            ),
        }

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden.")

        return cleaned_data
        