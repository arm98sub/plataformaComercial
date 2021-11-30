from django import forms
from .models import Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario

        fields = ('first_name','username','password', 'password2','email','foto','estado','municipio')

        widgets = {
            'password': forms.PasswordInput(),
            'password2': forms.PasswordInput(),
            'estado': forms.Select()
        }

    def save(self, commit=True):
        user = super(UsuarioForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
    
    
    def clean_password(self, *args, **kwargs):
        if self.data['password'] != self.data['password2']:
            raise forms.ValidationError("Las contraseñas no coinciden")
        return self.data['password']