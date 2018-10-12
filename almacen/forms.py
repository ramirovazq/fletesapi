from django import forms

class FilterForm(forms.Form):

    picking = forms.CharField(
                required=False,
            label='Picking', 
            max_length="100",
            widget=forms.TextInput(
                attrs={
                'class':'form-control',
                'placeholder':'Ejemplo: WH/IN/0000X'
                }
    ))
    producto = forms.CharField(
                required=False,
                label='Producto', 
                max_length="250",
                widget=forms.TextInput(
                    attrs={
                    'class':'form-control',
                    'placeholder':'Ejemplo: Filtro'
                    }
    ))
    compania = forms.CharField(
                required=False,
                label='Compañía o Tractor', 
                max_length="250",
               widget=forms.TextInput(
                   attrs={
                   'class':'form-control',
                   'placeholder':'Ejemplo: T23'
                   }
    ))
    propietario = forms.CharField(
                required=False,
                label='Propietario', 
                max_length="190",
                widget=forms.TextInput(
                attrs={ 
                'class':'form-control',
                'placeholder':'Ejemplo: Mecánico'
                }
    ))
    detalle = forms.CharField(
                required=False,
                label='Detalle', 
                max_length="190",
                widget=forms.TextInput(
                attrs={ 
                'class':'form-control',
                'placeholder':'Ejemplo: Thermos'
                }
    ))

    fecha_creacion_inicio = forms.DateField(
                required=False,
                label='Fecha creacion inicio', 
                input_formats=["%d-%m-%Y"],
                widget=forms.TextInput(
                attrs={ 
                'class':'form-control',
                'placeholder':'dd-mm-yyyy'
                }
    ))
    fecha_creacion_fin = forms.DateField(
                required=False,
                label='Fecha creacion fin',
                input_formats=["%d-%m-%Y"],
                widget=forms.TextInput(
                attrs={ 
                'class':'form-control',
                'placeholder':'dd-mm-yyyy'
                }
    ))

    ultima_actualizacion_inicio = forms.DateField(
                required=False,
                label='Última actualización inicio',
                input_formats=["%d-%m-%Y"],
                widget=forms.TextInput(
                attrs={ 
                'class':'form-control',
                'placeholder':'dd-mm-yyyy'
                }
    ))
    ultima_actualizacion_fin = forms.DateField(
                required=False,
                label='Última actualización fin',
                input_formats=["%d-%m-%Y"],
                widget=forms.TextInput(
                attrs={ 
                'class':'form-control',
                'placeholder':'dd-mm-yyyy'
                }
    ))
    fecha_programada_inicio = forms.DateField(
                required=False,
                label='Fecha programada inicio',
                input_formats=["%d-%m-%Y"],
                widget=forms.TextInput(
                attrs={ 
                'class':'form-control',
                'placeholder':'dd-mm-yyyy'
                }
    ))

    fecha_programada_fin = forms.DateField(
                required=False,
                label='Fecha programada fin',
                input_formats=["%d-%m-%Y"],
                widget=forms.TextInput(
                attrs={ 
                'class':'form-control',
                'placeholder':'dd-mm-yyyy'
                }
    ))

