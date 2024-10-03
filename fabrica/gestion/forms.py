#asi creamos formulario de una manera facil en djago importamos esta libreria
from django import forms

#cada clase es un formulario le pasamos como parametro pues forms
class Buscar_Persona (forms.Form):
    
    #aqui creamos una especie de tupla / diccionario donde lo que esta a la izquierda
    #es lo que se retorna como variable y a la derecha el valor que se muestra
    OPCIONES_BUSQUEDA = [
        ('trabajador', 'Trabajador'),
        ('postulante', 'Postulante'),
        ('despedido', 'Despedido'),
    ]

    #creamos un campo para introducir nombre
    nombre = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Nombre de la persona a buscar', 'maxlength': '200', 'style': 'width:200px;', 'size': '35'}))
    
    #y este es un segundo campo donde le dice que tendra 3 opciones y que seran de 
    #selecionar a manera una barra desplegable
    tipo_busqueda = forms.ChoiceField(
        choices=OPCIONES_BUSQUEDA,
        widget=forms.Select
    )

#creamos un segundo formulario y 3 campos los dos primeros normal como ya sabemos    
class Contacto (forms.Form):
    
    asunto = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Ingrese Un Asunto'}))
    
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Ingrese su correo electrónico', ' maxlength': '100','style': 'width:70%;'}))
    
    #aca le especificamos que sera ancho como un texarea y los atributos seran estos
    mensaje = forms.CharField(widget=forms.Textarea(attrs={'rows': 10, 'cols': 70}))
