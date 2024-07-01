from django.shortcuts import render, redirect
from django.contrib import messages
from miapp.forms import FormEstudiante
from miapp.models import estudiante
# Create your views here.

def integrantes(request):
    return render(request, 'integrantes.html',{
        'titulo': 'Integrantes'
    })
    

def saludo(request):
    return render(request, 'saludo.html',{
        'titulo': 'Saludo'
    })

def create_estudiante(request):
    if request.method == 'POST':
        formulario = FormEstudiante(request.POST)
        if formulario.is_valid():
            data_form = formulario.cleaned_data
            # Hay 2 formas de recuperar la información
            codigo = data_form.get('codigo')
            dni = data_form['dni']
            nombre = data_form['nombre']
            apepat = data_form['apepat']
            apemat = data_form['apemat']
            direccion = data_form['direccion']
            telefono = data_form['telefono']
            estado = data_form['estado']
            
            nuevo_estudiante = estudiante(
                codigo=codigo,
                dni=dni,
                nombre=nombre,
                apepat=apepat,
                apemat=apemat,
                direccion=direccion,
                telefono=telefono,
                estado=estado
            )
            nuevo_estudiante.save()
            
            # Crear un mensaje flash (Sesión que solo se muestra 1 vez)
            messages.success(request, f'Se agregó correctamente el estudiante con código {nuevo_estudiante.codigo}')
            return redirect('listar_estudiantes')
    else:
        formulario = FormEstudiante()
        # Generamos un formulario vacío

    return render(request, 'create_estudiante.html', {
        'titulo': 'Crear Estudiante',
        'form': formulario
    })

def listar_estudiantes(request):
    estudiantes = estudiante.objects.all();
    return render(request, 'listar_estudiantes.html',{
        'estudiantes': estudiantes,
        'titulo': 'Listado de Estudiantes'
    })