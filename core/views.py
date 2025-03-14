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

from django.shortcuts import render, redirect, get_object_or_404
from .models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone

@login_required(login_url='/login/')
def lista_eventos(request):
    usuario = request.user
    eventos = Evento.objects.filter(usuario=usuario)
    dados = {'eventos': eventos}
    return render(request, 'Agenda.html', dados)

def index(request):
    return render(request, 'index.html')

@login_required(login_url='/login/')
def evento(request):
    id_evento = request.GET.get('id')
    evento = get_object_or_404(Evento, id=id_evento) if id_evento else None
    return render(request, 'evento.html', {'evento': evento})

def criar_evento(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        data_evento_str = request.POST.get('data_evento')
        descricao = request.POST.get('descricao')
        usuario = request.user

        if titulo and data_evento_str and descricao:
            try:
                data_evento = timezone.datetime.fromisoformat(data_evento_str)
                Evento.objects.create(titulo=titulo, data_evento=data_evento, descricao=descricao, usuario=usuario)
                messages.success(request, "Evento criado com sucesso!")
                return redirect('/agenda/')
            except ValueError:
                messages.error(request, "Formato de data/hora inválido.")
                return redirect('/agenda/evento/')
            except Exception as e:
                messages.error(request, f"Erro ao criar evento: {e}")
                return redirect('/agenda/evento/')
        else:
            messages.error(request, "Preencha todos os campos.")
            return redirect('/agenda/evento/')
    else:
        return redirect('/agenda/evento/')

def editar_evento(request, id_evento):
    evento = get_object_or_404(Evento, id=id_evento)
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        data_evento_str = request.POST.get('data_evento')
        descricao = request.POST.get('descricao')

        if titulo and data_evento_str and descricao:
            try:
                data_evento = timezone.datetime.fromisoformat(data_evento_str)
                evento.titulo = titulo
                evento.data_evento = data_evento
                evento.descricao = descricao
                evento.save()
                messages.success(request, "Evento atualizado com sucesso!")
                return redirect('/agenda/')
            except ValueError:
                messages.error(request, "Formato de data/hora inválido.")
                return redirect('/agenda/evento/?id='+str(id_evento))
            except Exception as e:
                messages.error(request, f"Erro ao atualizar evento: {e}")
                return redirect('/agenda/evento/?id='+str(id_evento))
        else:
            messages.error(request, "Preencha todos os campos.")
            return redirect('/agenda/evento/?id='+str(id_evento))
    else:
        return render(request, 'evento.html', {'evento': evento})

def login_user(request):
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('/')

@login_required(login_url='/login/')
def delete_evento(request, id_evento):
    usuario = request.user
    evento = get_object_or_404(Evento, id=id_evento)
    if usuario == evento.usuario:
        evento.delete()
    return redirect('/agenda/')

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
            return redirect('/login/')
    else:
        return redirect('/login/')