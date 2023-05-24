from django import forms

class LoginForms(forms.Form):
    nome_login = forms.CharField(
        label='Nome de Login:',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder':  'Ex.:João Silva',
            }
        ),
    )
    
    senha = forms.CharField(
        label='Senha:',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite sua senha',
            }
        ),
    )
    
class CadastroForms(forms.Form):
    nome_cadastro=forms.CharField(
        label='Nome de Cadastro',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Ex.:João Silva',
            }
        ),
    )
    
    email = forms.EmailField(
        label='Email:',
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: email@outlook.com',
            }
        ),
    )
    
    senha_1=forms.CharField(
        label='Senha:',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder': 'Digite sua Senha:'
            }
        ),
    )
    
    senha_2=forms.CharField(
        label='Senha:',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder': 'Digite sua Senha novamente:'
            }
        ),
    )
    
class Cadastrados(forms.Form):
   nome = forms.CharField(max_length=255)
   nasc = forms.CharField(max_length=20)
   idade = forms.IntegerField()
   genero = forms.CharField(max_length=50)
   naturalidade = forms.CharField(max_length=50)
   tempo = forms.IntegerField()
   cpf = forms.CharField(max_length=11)
   rg = forms.CharField(max_length=20)
   nis = forms.CharField(max_length=20)
   sus = forms.CharField(max_length=20)
   mae = forms.CharField(max_length=255)
   pai = forms.CharField(max_length=255)
   resp = forms.CharField(max_length=255)
   parentesco = forms.CharField(max_length=50)
   end = forms.CharField(max_length=150)
   bairro = forms.CharField(max_length=100)
   cidade = forms.CharField(max_length=100)
   estado = forms.CharField(max_length=50)
   tel = forms.IntegerField()
   cel = forms.IntegerField()
   enc = forms.CharField(max_length=100)
   motivo = forms.CharField(max_length=100)