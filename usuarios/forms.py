from django import forms
from .models import Usuario, Usuario_Vendedor
from django.contrib.auth.models import Group

# Clase que implementa un tipo de usuario personalizado.


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario

        fields = ('first_name','username','password', 'password2','email','foto')

        widgets = {
            'password': forms.PasswordInput(),
            'password2': forms.PasswordInput(),
            'estado': forms.Select()
        }

    # Método por el cual se guardan los usuarios.
    def save(self, commit=True):
        user = super(UsuarioForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

    # Verifica que las contraseñas ingresadas coinsidan
    def clean_password(self, *args, **kwargs):
        if self.data['password'] != self.data['password2']:
            raise forms.ValidationError("Las contraseñas no coinciden")
        return self.data['password']

# Clase de usuario vendedor


class Usuario_Vendedor_Form(forms.ModelForm):
    class Meta:
        model = Usuario_Vendedor

        # Campos que tendra este usuario.
        fields = ('first_name', 'username', 'password', 'password_rev', 'email', 'foto', 'direccion','telefono', 'descripcion')
        
        # Se especifica el tipo de widget que sera utilizado para algunos de los campos.
        widgets = {
            'password': forms.PasswordInput(),
            'password_rev': forms.PasswordInput(),
            'descripcion': forms.Textarea()
        }

    # Guarda al usuario registrado.
    def save(self, commit=True):
        user = super(Usuario_Vendedor_Form, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            my_group = Group.objects.get(name='vendedores')
            user.save()
            my_group.user_set.add(user)
        return user

    # Verifica que la contraseña ingresada y la confirmacion sean iguales, de lo contrario, la limpia.
    def clean_password(self, *args, **kwargs):
        if self.data['password'] != self.data['password_rev']:
            raise forms.ValidationError("Las contraseñas no coinciden")
        return self.data['password']
