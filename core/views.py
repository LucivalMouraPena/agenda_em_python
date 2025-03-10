"""from django.shortcuts import render

from core.models import Evento

# Create your views here.

def lista_eventos(request):
    evento = Evento.objects.all()
    response = {'eventos': evento}
    return render(request, 'Agenda.html', dados)
""" 
# deixei o codigo acima comentado para verificar se  esse abaixo, se está correto   

from django.shortcuts import render, redirect
from core.models import Evento

def index(request):
    return redirect('/agenda/')
def lista_eventos(request):
    evento = Evento.objects.all()
    response = {'eventos': evento}
    return render(request, 'Agenda.html', response)  # Corrigido aqui