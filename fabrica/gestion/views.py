from django.shortcuts import render, HttpResponse #importamos esto para que de una especie de pagina web
from django.core.mail import send_mail #esta libreria es para enviar mails
from gestion.forms import Buscar_Persona, Contacto #importamos los formularios que creamos
from gestion.models import Trabajador,Postulante,Despedido #ahora importamos las tablas de las bd


# Create your views here.

#usamos render y le indicamos que pase el html pero que esta en la carpeta templates
#gestionApp/todos los html
def inicio (request):
    
    return render(request,'gestionApp/inicio.html')

#asi le devolvemos otra html pero como ctnx el formulario que creamos lo iniciamos asi
def buscar (request):
    
    formulario = Buscar_Persona()
    
    return render(request,'gestionApp/buscar.html',{'formulario': formulario})

#aca estara lo que nos restorne del html buscar
def encuentra (request):
    
    #primero llena el formulario con lo retornado por medio del get en esta variable
    formulario = Buscar_Persona(request.GET)
            
    # y si es valido entra aca o sea si los datos estan bien        
    if formulario.is_valid():
        
        #de esta forma almacenamos todos los datos aca en una especie de lista diccionaio   
        info_formulario = formulario.cleaned_data
        
        #a cada variable le asignamos un valor del campo del formulario 
        nombre = info_formulario['nombre']
        tabla_buscar_bd = info_formulario['tipo_busqueda']
        
        #creamos esto para de esta forma colocar la instruccion y buscar en la bd
        tablas = [Trabajador, Postulante, Despedido]
        
        # y si encuentra algo lo vamos almacenar en esta lista   
        resultados_buscar_bd = []
        
        #para que funcione si o si le debemos dar.lower de esta forma le recordamos que es un str para
        #que funcione la comparacion y asi hacemos con las demas tabla para buscar en la bd    
        if tabla_buscar_bd.lower() == 'trabajador':
            
            #almacenamos lo encontrado en la lista a manera de extends le indicamos la tabla a buscar
            #indicandole la posicion de la lista tablas que creamos arriba introducimos la instruccion
            #para filtrar y lo vamos a filtrar por variable__icontains debe ser igual a..
            resultados_buscar_bd.extend(tablas[0].objects.filter(nombre__icontains = nombre))
                
        elif tabla_buscar_bd.lower() == 'postulante':
                
            resultados_buscar_bd.extend(tablas[1].objects.filter(nombre__icontains = nombre))
                
        else:
                
            resultados_buscar_bd.extend(tablas[2].objects.filter(nombre__icontains = nombre))
                
        #si lo almacenado en la lista de resultados es iterable seguimos con el procedimiento      
        if any(resultados_buscar_bd):
            
            #pasamos un ctnx donde pasamos lo buscado, si encontramos y la tabla
            ctnx = {
                
                'introducido': nombre,
                'encontrado': resultados_buscar_bd,
                'tabla' : tabla_buscar_bd
                
                }
            
            #y solo entonces retornamos el html de encuentra
            return render(request, 'gestionApp/encuentra.html', ctnx)
        
        #de lo contrario usando el response le pasamos un mensaje diciendo que no fue posible encontrar   
        else:
                
            mensaje = 'Persona no encontrada'
                
            return HttpResponse(mensaje)
        
    else:
        
        mensaje = 'Lo introducido en el formulario no es valdo\nPor fravor regrese a la anterior pagiona.'
        
        return HttpResponse(mensaje)

#aca le pasamos directamente una vista para que nos envie un gmail a un correo especifico
def contacto (request): 
    
    #aca verificamos si se uso el metodo post
    if request.method == 'POST':
        
        #llenamos el formulario con lo retornado en el metodo
        enviado_formulario = Contacto(request.POST)
        
        #verificamos si es valido
        if enviado_formulario.is_valid():
            
            #accedemos a la informacion es una especie de lista diccionario
            obteniento_texto = enviado_formulario.cleaned_data
            
            #cree esta variable mensaje a manera de que me devuelva el gmail de la persona que debo contactar
            #accedemos a los compaos intruducidos de esrta forma
            mensaje = obteniento_texto['mensaje'] + "\nEl email es: " + obteniento_texto['email']
            
            #accemos a send para que nos envie un gmail
            #primero le pasamos asunto, mensaje. Luego le decimos que el email sera el que especificamos en settings
            # o sea de donde se va a enviar se puede dejar vacia ya que lo configuramos en settings
            #y por ultimo en forma de list el gmail a donde deve llegar
            send_mail(obteniento_texto['asunto'],mensaje, obteniento_texto.get('email',''), ['invinciboy0@gmail.com'],)
            
            #y le decimos que crea una vista donde retorne esto
            return HttpResponse('Mensaje enviado')
    
    #si no se ha usado el mtodo post pues creamos el formulario vacio pasamos el html contacto con un ctnx o sea el
    #formulario
    else:
        
        formulario = Contacto()
        
        return render(request,'gestionApp/contacto.html',{'formulario': formulario})
        
            
        
