from django import forms
from django.core import validators

class FormEstudiante(forms.Form):
    codigo = forms.CharField(
        label="Código",
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Ingrese el código',
                'class': 'codigo_form_estudiante'
            }
        )
    )

    dni = forms.CharField(
        label="DNI",
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Ingrese el DNI',
                'class': 'dni_form_estudiante'
            }
        ),
        validators=[
            validators.RegexValidator('^\d{8}$', 'El DNI debe tener 8 dígitos', 'dni_invalido')
        ]
    )

    nombre = forms.CharField(
        label="Nombre",
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Ingrese el nombre',
                'class': 'nombre_form_estudiante'
            }
        ),
        validators=[
            validators.MinLengthValidator(2, 'El nombre es muy corto'),
            validators.RegexValidator('^[A-Za-zñÑáéíóúÁÉÍÓÚ ]*$', 'El nombre tiene caracteres inválidos', 'nombre_invalido')
        ]
    )

    apepat = forms.CharField(
        label="Apellido Paterno",
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Ingrese el apellido paterno',
                'class': 'apepat_form_estudiante'
            }
        )
    )

    apemat = forms.CharField(
        label="Apellido Materno",
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Ingrese el apellido materno',
                'class': 'apemat_form_estudiante'
            }
        )
    )

    direccion = forms.CharField(
        label="Dirección",
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Ingrese la dirección',
                'class': 'direccion_form_estudiante'
            }
        )
    )

    telefono = forms.CharField(
        label="Teléfono",
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Ingrese el teléfono',
                'class': 'telefono_form_estudiante'
            }
        ),
        validators=[
            validators.RegexValidator('^\d{9}$', 'El teléfono debe tener 9 dígitos', 'telefono_invalido')
        ]
    )

    estado = forms.ChoiceField(
        label="Estado",
        choices=[
            (1, 'Activo'),
            (0, 'Inactivo')
        ],
        required=True,
        widget=forms.Select(
            attrs={
                'class': 'estado_form_estudiante'
            }
        )
    )