from webClaro.models import Cliente, Comuna, ImagenPerfil, TecnologiaServicio, ServicioContratado, PlanContratado
from webClaro.models import CantidadDecodificadores, EstadoInstalacion
from django.shortcuts import render


# PARA LOGIN ###################################################################
# Tabla Usuarios del sistema
from django.contrib.auth.models import User

# Validaciones de login
from django.contrib.auth import authenticate, logout, login as login_aut

# Decoradores
from django.contrib.auth.decorators import login_required
###################################################################

# Create your views here.
@login_required(login_url='/login/')
def index(request):
    img = ImagenPerfil.objects.filter(usuario = request.user.username)
    clientes = Cliente.objects.filter(vendedor = request.user.username).order_by('-fechaInstalacion')
    
    # Método ir a Index.
    contadorClientes = Cliente.objects.filter(vendedor = request.user.username).count()
    deco1 = clientes.filter(cantidadDecos = 1).count()
    deco2 = clientes.filter(cantidadDecos = 2).count()
    deco3 = clientes.filter(cantidadDecos = 3).count()
    deco4 = clientes.filter(cantidadDecos = 4).count()
    contadorDecos = deco1 + (deco2 * 2) + (deco3 * 3) + (deco4 * 4)
    contadorBafis = clientes.filter(servicioContratado__contains = "BAFI").count()

    return render(request, "index.html", {"img": img, "clientes":clientes, "cantClientes":contadorClientes, "cantDecos":contadorDecos, "cantBafis":contadorBafis})
    
def login(request):
    mensaje = ''

    if request.POST:
        user = request.POST.get("txtUsuario")
        contrasena = request.POST.get("txtPassword")
        acceso = authenticate(request, username = user, password = contrasena)

        if acceso is not None and acceso.is_active:
            login_aut(request, acceso)

            # Método ir a Index.
            img = ImagenPerfil.objects.filter(usuario = request.user.username)
            clientes = Cliente.objects.filter(vendedor = request.user.username).order_by('-fechaInstalacion')
            contadorClientes = Cliente.objects.filter(vendedor = request.user.username).count()
            deco1 = clientes.filter(cantidadDecos = 1).count()
            deco2 = clientes.filter(cantidadDecos = 2).count()
            deco3 = clientes.filter(cantidadDecos = 3).count()
            deco4 = clientes.filter(cantidadDecos = 4).count()
            contadorDecos = deco1 + (deco2 * 2) + (deco3 * 3) + (deco4 * 4)
            return render(request, "index.html", {"img": img, "clientes":clientes, "cantClientes":contadorClientes, "cantDecos":contadorDecos})

        else:
           mensaje = "Usuario o contraseña incorrectos"

    return render(request, "login.html", {"mensaje":mensaje})

@login_required(login_url='/login/')
def verCliente(request, id):
    cliente = Cliente.objects.get(id = id)
    img = ImagenPerfil.objects.filter(usuario = request.user.username)
    whatsapp = cliente.telefono.strip()
    whatsappTrim = whatsapp.replace(" ", "")

    return render(request, "cliente.html", {"img": img, "cliente":cliente, "whatsapp":whatsappTrim})

@login_required(login_url='/login/')
def registroCliente(request):
    mensaje = ''

    if request.POST:
        nombre = request.POST.get("txtNombre")
        rut = request.POST.get("txtRUT")
        direccion = request.POST.get("txtDireccion")
        telefono = request.POST.get("txtTelefono")
        servicio = request.POST.get("selServicio")
        tecnologia = request.POST.get("selTecnologia")
        plan = request.POST.get("selPlan")
        decos = request.POST.get("selDecos")
        costoInst = request.POST.get("txtCostoInst")
        fecha = request.POST.get("inpFecha")
        vendedor = request.user.username
        servTecn = servicio + ' ' + tecnologia
        estado = request.POST.get("selEstado")
        comentarios = request.POST.get("txtComentarios")
        comuna = request.POST.get("selComuna")
        objComuna = Comuna.objects.get(nombre = comuna)
        
        cliente = Cliente()
        cliente.nombre = nombre
        cliente.rut = rut
        cliente.direccion = direccion
        cliente.telefono = telefono
        cliente.servicioContratado = servicio
        cliente.tecnologiaServicio = tecnologia
        cliente.planContratado = plan
        cliente.cantidadDecos = decos
        cliente.costoInstalacion = costoInst
        cliente.fechaInstalacion = fecha
        cliente.vendedor = vendedor
        cliente.servicioTecnologia = servTecn
        cliente.estado = estado
        cliente.Comuna = objComuna

        if comentarios is not None:
            cliente.comentarios = comentarios

        cliente.comentarios = "Sin observaciones."

        cliente.save()
        mensaje = "Cliente registrado exitosamente."

    img = ImagenPerfil.objects.filter(usuario = request.user.username)
    objComuna = Comuna.objects.all()

    return render(request, "registroCliente.html", {"img": img, "comunas":objComuna, "mensaje":mensaje})

@login_required(login_url='/login/')
def perfil(request):
    img = ImagenPerfil.objects.filter(usuario = request.user.username)
    return render(request, "perfil.html", {"img": img})

@login_required(login_url='/login/')
def cerrarSesion(request):
    logout(request)
    mensaje = "Has cerrado sesión correctamente."
    return render(request, "login.html", {"mensaje":mensaje})

@login_required(login_url='/login/')
def modificarCliente(request, id):
    mensaje = ''
    
    try:
        cliente = Cliente.objects.get(id = id)
        img = ImagenPerfil.objects.filter(usuario = request.user.username)
        objComuna = Comuna.objects.all()
        objServicioContratado = ServicioContratado.objects.all()
        objTecnologiaServicio = TecnologiaServicio.objects.all()
        objPlanContratado = PlanContratado.objects.all()
        objCantidadDecodificadores = CantidadDecodificadores.objects.all()
        objEstadoInstalacion = EstadoInstalacion.objects.all()
        return render(request, "modifCliente.html", {"img": img, "comunas":objComuna, "cliente":cliente, "servicios":objServicioContratado, "tecnologias":objTecnologiaServicio, "planes":objPlanContratado, "decos":objCantidadDecodificadores, "estados":objEstadoInstalacion})

    except Exception as e:
        mensaje = "No existe el cliente."
        print(e)

    # Método ir a Index.
    img = ImagenPerfil.objects.filter(usuario = request.user.username)
    clientes = Cliente.objects.filter(vendedor = request.user.username).order_by('-fechaInstalacion')
    contadorClientes = Cliente.objects.filter(vendedor = request.user.username).count()
    deco1 = clientes.filter(cantidadDecos = 1).count()
    deco2 = clientes.filter(cantidadDecos = 2).count()
    deco3 = clientes.filter(cantidadDecos = 3).count()
    deco4 = clientes.filter(cantidadDecos = 4).count()
    contadorDecos = deco1 + (deco2 * 2) + (deco3 * 3) + (deco4 * 4)
    contadorBafis = clientes.filter(servicioContratado__contains = "BAFI").count()

    return render(request, "index.html", {"img": img, "clientes":clientes, "cantClientes":contadorClientes, "cantDecos":contadorDecos, "cantBafis":contadorBafis, "mensaje":mensaje})


def actualizarCliente(request):
    mensaje = ''

    if request.POST:
        id = request.POST.get("txtId")
        nombre = request.POST.get("txtNombre")
        rut = request.POST.get("txtRUT")
        direccion = request.POST.get("txtDireccion")
        telefono = request.POST.get("txtTelefono")
        servicio = request.POST.get("selServicio")
        tecnologia = request.POST.get("selTecnologia")
        plan = request.POST.get("selPlan")
        decos = request.POST.get("selDecos")
        costoInst = request.POST.get("txtCostoInst")
        fecha = request.POST.get("inpFecha")
        vendedor = request.user.username
        servTecn = servicio + ' ' + tecnologia
        estado = request.POST.get("selEstado")
        comentarios = request.POST.get("txtComentarios")
        comuna = request.POST.get("selComuna")
        objComuna = Comuna.objects.get(nombre = comuna)
        
        cliente = Cliente.objects.get(id = id)

        try:
            cliente.nombre = nombre
            cliente.rut = rut
            cliente.direccion = direccion
            cliente.telefono = telefono
            cliente.servicioContratado = servicio
            cliente.tecnologiaServicio = tecnologia
            cliente.planContratado = plan
            cliente.cantidadDecos = decos
            cliente.costoInstalacion = costoInst
            cliente.fechaInstalacion = fecha
            cliente.vendedor = vendedor
            cliente.servicioTecnologia = servTecn
            cliente.estado = estado
            cliente.Comuna = objComuna

            if comentarios is not None:
                cliente.comentarios = comentarios

            cliente.comentarios = "Sin observaciones."

            cliente.save()
            mensaje = "Cliente modificado exitosamente."
        
        except:
            mensaje = "Cliente no modificado."

    # Método ir a Index.
    img = ImagenPerfil.objects.filter(usuario = request.user.username)
    clientes = Cliente.objects.filter(vendedor = request.user.username).order_by('-fechaInstalacion')
    contadorClientes = Cliente.objects.filter(vendedor = request.user.username).count()
    deco1 = clientes.filter(cantidadDecos = 1).count()
    deco2 = clientes.filter(cantidadDecos = 2).count()
    deco3 = clientes.filter(cantidadDecos = 3).count()
    deco4 = clientes.filter(cantidadDecos = 4).count()
    contadorDecos = deco1 + (deco2 * 2) + (deco3 * 3) + (deco4 * 4)
    contadorBafis = clientes.filter(servicioContratado__contains = "BAFI").count()

    return render(request, "index.html", {"img": img, "clientes":clientes, "cantClientes":contadorClientes, "cantDecos":contadorDecos, "cantBafis":contadorBafis, "mensaje":mensaje})