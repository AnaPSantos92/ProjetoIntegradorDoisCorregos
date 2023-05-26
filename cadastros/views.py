from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from cadastros.forms import LoginForms, CadastroForms, CadastradosForms
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from .models import Cadastrados
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView


def index(request):
    return render(request, 'index.html')


def login(request):
    form = LoginForms()

    if request.method == 'POST':
        form = LoginForms(request.POST)

        if form.is_valid():
            nome_login = form['nome_login'].value()
            senha = form['senha'].value()

        nome_login = auth.authenticate(
            request,
            username=nome_login,
            password=senha
        )

        if nome_login is not None:
            auth.login(request, nome_login)
            messages.success(request, 'Logado com sucesso!')
            return redirect('indexcompleta')
        else:
            messages.error(request, 'Erro ao efetuar login')
            return redirect('login')
    return render(request, 'login.html', {'form': form})


def logincadastrar(request):
    form = CadastroForms()

    if request.method == 'POST':
        form = CadastroForms(request.POST)

        if form.is_valid():
            if form["senha_1"].value() != form["senha_2"].value():
                messages.error(request, 'Senhas não são iguais!')
                return redirect('logincadastrar')

            nome = form['nome_cadastro'].value()
            email = form['email'].value()
            senha = form['senha_1'].value()

            if User.objects.filter(username=nome).exists():
                messages.error(request, 'Usuários já existente!')
                return redirect('logincadastrar')

            usuario = User.objects.create_user(
                username=nome,
                email=email,
                password=senha
            )

            usuario.save()
            messages.success(request, 'Cadastro efetuado com sucesso!')
            return redirect('login')

    return render(request, 'logincadastrar.html', {'form': form})


def indexcompleta(request):
    return render(request, 'indexcompleta.html')


def cadastrar(request):
    return render(request, 'cadastrar.html')


def consultar(request):
    return render(request, 'consultar.html')


def usuarioscadastrados(request):
    novo_usuario = Cadastrados()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.nasc = request.POST.get('nasc')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.genero = request.POST.get('genero')
    novo_usuario.naturalidade = request.POST.get('naturalidade')
    novo_usuario.tempo = request.POST.get('tempo')
    novo_usuario.cpf = request.POST.get('cpf')
    novo_usuario.rg = request.POST.get('rg')
    novo_usuario.nis = request.POST.get('nis')
    novo_usuario.sus = request.POST.get('sus')
    novo_usuario.mae = request.POST.get('mae')
    novo_usuario.pai = request.POST.get('pai')
    novo_usuario.resp = request.POST.get('resp')
    novo_usuario.parentesco = request.POST.get('parentesco')
    novo_usuario.end = request.POST.get('end')
    novo_usuario.bairro = request.POST.get('bairro')
    novo_usuario.cidade = request.POST.get('cidade')
    novo_usuario.estado = request.POST.get('estado')
    novo_usuario.tel = request.POST.get('tel')
    novo_usuario.cel = request.POST.get('cel')
    novo_usuario.enc = request.POST.get('enc')
    novo_usuario.motivo = request.POST.get('motivo')
    confere = Cadastrados.objects.all()
    aux = True
    for i in confere:
        if novo_usuario.cpf == i.cpf:
            aux = False
    if aux == True:
        novo_usuario.save()
    
    
    usuarios = {
        'usuarios': Cadastrados.objects.all()
    }
    
    return render(request, 'usuarioscadastrados.html', usuarios)

def logout(request):
    auth.logout(request)
    messages.success(request, 'Logout efetuado com sucesso!')
    return redirect('inicio')

def listausuarios(request):
    usuarios = {
        'usuarios': Cadastrados.objects.all()
    }
    
    return render(request, 'listausuarios.html', usuarios)



class UsuariosList(ListView):
    model = Cadastrados
    template_name = 'listausuarios.html'
    

    def get_queryset(self):

        txt_cpf = self.request.GET.get('cpf')

        if txt_cpf:
            busca = Cadastrados.objects.filter(cpf__contains='txt_cpf')
        else:
            busca = Cadastrados.objects.all()

        return busca 

def buscar(request):
    usuarios = Cadastrados.objects.all()
    
    if "cpf" in request.GET:
        nome_a_buscar = request.GET['cpf']
        if nome_a_buscar:
            usuarios = usuarios.filter(cpf__icontains=nome_a_buscar)
            
    return render(request, 'buscar.html', {"usuarios": usuarios})


""" def editar(request, novo_usuario_id):
    resultado = Cadastrados.objects.get(id=novo_usuario_id)
    form = Cadastrados(resultado)
    
    if request.method == "POST":
        form = Cadastrados(request.POST, request.FILES, resultado)
        if form.is_valid():
            form.save()
            messages.success(request, 'Editado com sucesso!')
            return redirect('listausuarios')
    
    return render(request, 'editar.html', {"form": form, 'novo_usuario_id': novo_usuario_id}) """
    
def editar(request):
    return render(request, "editar.html")
    

def deletar(request, novo_usuario_id):
    resultado = Cadastrados.objects.get(id=novo_usuario_id)
    resultado.delete()
    messages.success(request, 'Exclusão efetuada com sucesso!')
    return redirect('listausuarios')

    # usuarios = Cadastrados.objects.all()
   # usuarios.delete()
    # return render(request, 'deletar.html')



    
    