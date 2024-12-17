from django import forms
from django.core import validators
from .models import Seminario, Instituciones
class InstitucionesForm(forms.ModelForm):
    class Meta:
        model = Instituciones
        fields = ('__all__')
    nombreInstituciones = forms.CharField(
        required=True,
        validators=[validators.MaxLengthValidator(80)]
    )
    nombreInstituciones.widget.attrs['class'] = 'form-control'

class SeminarioForm(forms.ModelForm):
    class Meta:
        model = Seminario
        fields = ('__all__')
    ESTADOS = [
        ('Reservado', 'RESERVADO'),
        ('Completada', 'COMPLETADA'),
        ('Anulada', 'ANULADA'),
        ('No Asisten', 'NO ASISTEN'),
    ]
    institucion = forms.ModelChoiceField(
        required=True,
        queryset = Instituciones.objects.all(),
        to_field_name = 'id',
        empty_label = "Seleccione una Institucion",
    )
    nroPersonas = forms.IntegerField(
        required=True,
        validators = [validators.MinValueValidator(1), 
                      validators.MaxValueValidator(30)]
    )
    telefono = forms.IntegerField(
        required=True
    )
    fechaInscripcion = forms.DateField(
        required=True,
        widget=forms.DateInput(attrs={'type': 'date'})
    )

    horaInscripcion = forms.TimeField(
        required=True,
        widget=forms.TimeInput(attrs={'type': 'time'})
    )
    email = forms.EmailField(widget=forms.EmailInput)
    
    estado = forms.CharField(
        required=True,
        widget=forms.Select(choices=ESTADOS)
    )
    observacion = forms.CharField(
        required=False,
    )


    institucion.widget.attrs['class'] = 'form-control'
    nroPersonas.widget.attrs['class'] = 'form-control'
    telefono.widget.attrs['class'] = 'form-control'
    fechaInscripcion.widget.attrs['class'] = 'form-control'
    horaInscripcion.widget.attrs['class'] = 'form-control'
    email.widget.attrs['class'] = 'form-control'
    estado.widget.attrs['class'] = 'form-select'
    observacion.widget.attrs['class'] = 'form-control'