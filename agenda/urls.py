"""
URL configuration for agenda project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views
'''
urlpatterns = [
    path('admin/', admin.site.urls),
    path('agenda/', views.lista_eventos),
    #path('', views.lista_eventos, name='home'),
    path('', views.index),
    path('/login/', viwes.login_user) 
]   

from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),  # Certifique-se de que o nome da view está correto aqui
    #path('eventos/', views.lista_eventos, name='lista_eventos'),coloquei abaixo a sugestao
    path('agenda/', views.lista_eventos, name='lista_eventos'),
    

] '''
'''
from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('agenda/', views.lista_eventos, name='lista_eventos'),  # Adicione esta linha
    path('eventos/', views.lista_eventos, name='lista_eventos'),
    path('login/', views.login_user, name='login_user'),
]
'''

from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
     path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('agenda/', views.lista_eventos, name='lista_eventos'),
    path('agenda/evento/', views.evento, name='evento'),
    path('agenda/evento/delete/<int:id_evento>', views.delete_evento, name='excluir_evento'),
    path('login/', views.login_user, name='login_user'),
    path('agenda/login/', views.login_user, name='agenda_login_user'),
    path('agenda/login/submit/', views.submit_login, name='submit_login'),
    path('logout/', views.logout_user, name='logout'),
    path('agenda/evento/criar/', views.criar_evento, name='criar_evento'),
    path('agenda/evento/editar/<int:id_evento>/', views.editar_evento, name='editar_evento'),
]