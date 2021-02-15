from django import forms
from django.contrib.auth.models import User



class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control",}))
    username = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", }))
    first_name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", }))
    email = forms.EmailField(widget=forms.TextInput(attrs={"class":"form-control", }))


    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = "Usuario"
        self.fields['first_name'].label = "Nombre"
        self.fields['last_name'].label = "Apellido"
        self.fields['email'].label = "Mail"
        self.fields['password'].label = "Contraseña"

    class Meta():
        model = User
        fields = ('username','first_name', 'last_name', 'email', 'password')


class UploadFileForm(forms.Form):
    file = forms.FileField()
