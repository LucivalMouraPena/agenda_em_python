"""from django.shortcuts import render

from core.models import Evento

# Create your views here.

def lista_eventos(request):
    evento = Evento.objects.all()
    response = {'eventos': evento}
    return render(request, 'Agenda.html', dados)
""" 
# deixei o codigo acima comentado para verificar se  esse abaixo, se está correto   

"""from django.shortcuts import render, redirect
from core.models import Evento

def login_user(request):
    return render (request, 'login.html')

def index(request):
    return redirect('/agenda/')
@login_required(login_url='/login/')
def lista_eventos(request):
    evento = Evento.objects.all()
    response = {'eventos': evento}
    return render(request, 'Agenda.html', response)  # Corrigido aqui"""

"""
from django.shortcuts import render
from core.models import Evento
from django.contrib.auth.decorators import login_required  # Importe login_required aqui

# ... (seu código restante)

@login_required(login_url='/login/')
def lista_eventos(request):
    evento = Evento.objects.all()
    response = {'eventos': evento}
    return render(request, 'Agenda.html', response)" """

'''from django.shortcuts import render
from core.models import Evento
from django.contrib.auth.decorators import login_required

def index(request):  # Defina a view index aqui
    return render(request, 'index.html')  # Ou outro template que você queira usar

@login_required(login_url='/login/')
def lista_eventos(request):
    evento = Evento.objects.all()
    response = {'eventos': evento}
    return render(request, 'Agenda.html', response)'''
'''
from django.shortcuts import render
from core.models import Evento
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'index.html')
def login_user(request):
    return render(request, 'login_user.html')

@login_required(login_url='/login/')
def lista_eventos(request):
    evento = Evento.objects.all()
    dados = {'eventos': evento}  # Corrija a criação do dicionário 'dados'
    return render(request, 'Agenda.html', dados) '''
'''
from django.shortcuts import render
from core.models import Evento
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'index.html')

def login_user(request):
    return render(request, 'login_user.html')

@login_required(login_url='/login/')
def lista_eventos(request):
    evento = Evento.objects.all()
    dados = {'eventos': evento}
    return render(request, 'Agenda.html', dados) '''

from django.shortcuts import render, redirect
from core.models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib import messages

def index(request):
    return render(request, 'index.html')

def login_user(request):
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('/')

def submit_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect("/")
        else:
            messages.error(request, "Usuário ou senha inválidos.")
            return redirect('/login/') #Redireciona para a página de login com a mensagem de erro.
    else:
        return redirect('/login/') #Redireciona para a página de login caso o método não seja POST.

@login_required(login_url='/login/')
def lista_eventos(request):
    usuario = request.user
    evento = Evento.objects.filter(usuario=usuario)
    dados = {'eventos': evento}
    return render(request, 'Agenda.html', dados)
