from django.urls import path
from .views import inicio, registro, loginView , logout_vista, HomeUsuario, jugar, resultado_pregunta, tablero, borrar_respondidas

urlpatterns = [
    path('', inicio, name='inicio'),
    path('HomeUsuario/', HomeUsuario, name='HomeUsuario'),
    path('login/', loginView, name='login'),
    path('logout_vista/', logout_vista, name='logout_vista'),
    path('registro/', registro, name='registro'),
    path('jugar/', jugar, name='jugar'),
    path('tablero/', tablero, name='tablero'),
    path('resultado/<int:pregunta_respondida_pk>/', resultado_pregunta, name='resultado'),
    path('borrar_respondidas/', borrar_respondidas, name='borrar_respondidas'),
]
