from django.core.exceptions import ObjectDoesNotExist
from django.http.response import Http404
from django.shortcuts import get_object_or_404, render,redirect
from .forms import RegistroFormulario, UsuarioLoginFormulario
from django.contrib.auth import authenticate, login, logout
from .models import QuizUsuario, Pregunta, PreguntasRespondidas
from django.contrib.auth.decorators import login_required


# Create your views here.
def inicio(request):
    context={
        'bienvenido':'Bievenido'
    }

    return render(request,'inicio.html', context)

@login_required(login_url='login')
def HomeUsuario(request):
    return render(request,'Usuario/home.html')

@login_required(login_url='login')
def tablero(request):
    total_usuarios_quiz = QuizUsuario.objects.order_by('-puntaje_total')[:20]
    contador = total_usuarios_quiz.count()

    context = {
        'usuario_quiz': total_usuarios_quiz,
        'contar_user':contador,
    }
    return render(request,'play/tablero.html',context)

@login_required(login_url='login')
def jugar(request):
    QuizUser, created= QuizUsuario.objects.get_or_create(usuario=request.user)
    
    if request.method == 'POST':
        pregunta_pk = request.POST.get('pregunta_pk')
        pregunta_respondida = QuizUser.intentos.select_related('pregunta').get(pregunta__pk=pregunta_pk)
        respuesta_pk = request.POST.get('respuesta_pk')

        try:
            opcion_seleccionada = pregunta_respondida.pregunta.opciones.get(pk=respuesta_pk)
        except ObjectDoesNotExist:
            raise Http404
        
        QuizUser.validar_intento(pregunta_respondida,opcion_seleccionada)
        return redirect('resultado', pregunta_respondida.pk)

    else:
        pregunta = QuizUser.obtener_nuevas_preguntas()
        if pregunta is not None:
            QuizUser.crear_intentos(pregunta)
        context = {
            'pregunta':pregunta
        }
    return render(request,'play/jugar.html',context)

@login_required(login_url='login')
def resultado_pregunta(request, pregunta_respondida_pk):
    respondida = get_object_or_404(PreguntasRespondidas, pk=pregunta_respondida_pk)

    context = {
        'respondida':respondida
    }

    return render(request,'play/resultados.html',context)


def loginView(request):
    titulo = 'loguin'
    form = UsuarioLoginFormulario(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        usuario = authenticate(username=username, password=password)
        login(request,usuario)
        return redirect('inicio')
    
    context = {
        'form':form,
        'titulo':titulo
    }
    return render(request,'Usuario/login.html',context)




def registro(request):
    titulo = 'Crear una cuenta'
    if request.method == 'POST':
        form = RegistroFormulario(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistroFormulario()

    context = {
        'form':form,
        'titulo':titulo
    }

    return render(request,'Usuario/registro.html', context)

def logout_vista(request):
    logout(request)
    return redirect('inicio')
    
def borrar_respondidas(self):
    PreguntasRespondidas.objects.all().delete()
    return redirect('jugar')


@login_required(login_url='login')
def Atencion(request):
    return render(request,'play/atencion.html')