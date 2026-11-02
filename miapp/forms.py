from django import forms

class ContactoForm(forms.Form):
    nombre = forms.CharField(
        max_length=100, 
        label="Nombre completo",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tu nombre'})
    )
    email = forms.EmailField(
        label="Correo electrónico",
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'nombre@ejemplo.com'})
    )
    telefono = forms.CharField(
        max_length=20, 
        required=False,  # Campo opcional según la tarea de la Clase 12
        label="Teléfono (Opcional)",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tu teléfono'})
    )
    mensaje = forms.CharField(
        label="Mensaje",
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Escribe tu consulta...'})
    )