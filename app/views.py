from django.views import generic
from django.shortcuts import render, redirect
from .forms import Agregar, Productoform
from django.urls import reverse_lazy
from .models import Producto
from compra.models import Compra, DetalleProducto
from django.contrib.auth.mixins import LoginRequiredMixin





##Agregar Productos
class AgregarProducto(LoginRequiredMixin, generic.FormView):
    """
    FormView para administrar el formulrio para agregar un producto.
    
    """
    
    form_class = Agregar #El formulario que se va a usar
    template_name = "agregar.html" #La dirección del template
    success_url = reverse_lazy('lista') #La url donde vamos a redirigir al usuario



    def form_valid(self, form):
        """
    Sobree escribo el from_valid para poder manejar el inventario en la base de datos y la modificacion del precio.

        """

        #Obtengo los datos del formulario y los guardo en variables procesados por .cleaned_data
        nombre = form.cleaned_data['nombre'].capitalize() #Capitaliza el nombre del producto para evitar duplicados.
        precio_base = form.cleaned_data['precio_base'] 
        porcentaje_ganancia = form.cleaned_data['porcentaje_ganancia']
        stock = form.cleaned_data['stock']
    
        #Intento obtener el producto de la base de datos, si no existe, lo crea con los datos del formulario.
        producto, created = Producto.objects.get_or_create(nombre=nombre,
            defaults={
            'precio_base': precio_base,
            'porcentaje_ganancia': porcentaje_ganancia,
            'stock': stock
            #En el diccionario "defaults" estan los datos que se van a guardar en la base de datos cuando created es verdadero, es decir, que el producto no existe.
            })

        if not created: #Si created es falso, entonces el producto ya existe y se actualiza el stock.
            producto.precio_base = precio_base
            producto.porcentaje_ganancia = porcentaje_ganancia
            #Guardamos el nuevo precio y el nuevo porcentaje

            producto.stock += stock
            #sumamos al stock la cantidad que se pase

            producto.save()
            #Guardamos el producto.
            mensaje = "Se catualizo un producto."
            
        else:
            #Si no, el producto ya se creo y se guardo por el metodo get_or_created
            mensaje = "Se creo un producto"


        
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['actual'] = 'agregar'
        return context


##Listar los porductos y obtener la compra activa del usuario
class ListarProductos(LoginRequiredMixin, generic.ListView):
    """
    ListView para que se listen los productos desde la db en el template tranquilamente sin funciones raras.
    
    """
    model = Producto #El modelo que se va a usar
    context_object_name = 'productos' #El nombre del contexto que se va a usar en el template
    template_name = 'listaProductos.html' #El template que se va a usar

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            compra = Compra.objects.get(usuario=self.request.user, estado=True)
            context['compra'] = compra
            context['detalles'] = DetalleProducto.objects.filter(compra=compra)
            
            # Calcular la cantidad en carrito para cada producto
            productos_en_carrito = {detalle.producto_id: detalle.cantidad for detalle in context['detalles']}
            for producto in context['productos']:
                producto.cantidad_en_carrito = productos_en_carrito.get(producto.id, 0)
        except Compra.DoesNotExist:
            context['compra'] = None
            context['detalles'] = None
            for producto in context['productos']:
                producto.cantidad_en_carrito = 0
        
        context['actual'] = 'lista'
        return context

##Buscar productos
def buscar_producto(request):
    query = request.GET.get('q')
    productos = Producto.objects.filter(nombre__icontains=query)
    context = {
        'productos': productos,
        'query': query,
    }
    try:#Pruebo a obtener la compra del usuario
        context['compra'] = Compra.objects.get(usuario=request.user, estado=True) #Se obtiene la compra del usuario y se guarda en el contexto con el nombre de compra.
        context['detalles'] = DetalleProducto.objects.filter(compra=context['compra']) #Se obtienen los detalles de la compra y se guardan en el contexto con el nombre de detalles.
    except Compra.DoesNotExist: #Si no existe la compra del usuario, se guarda None en el contexto.
        context['compra'] = None
        context['detalles'] = None

    return render(request, 'resultados.html', context)


##Lista para modificar productos
class Modificar_producto(LoginRequiredMixin, generic.ListView):
    model = Producto 
    context_object_name = 'productos'
    template_name = 'modificar_producto.html'
    
## Funcion para modificar productos
def modificar_producto(request, pk):
    producto = Producto.objects.get(pk=pk)
    if request.method == 'POST':
        form = Productoform(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('modificar_producto')

    else:
        form = Productoform(instance=producto)

    return render(request, 'producto_modificar.html', {'form': form, 'producto': producto})








