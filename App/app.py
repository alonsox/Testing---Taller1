from Dominio.RepositorioUsuarios import RepositorioUsuarios
from Dominio.Usuario import Usuario
from Dominio.Correo import Correo
from Dominio.Contraseña import Contraseña
from Pantallas.MenuNavegacion import MenuNavegacion
from Pantallas.MenuPrincipal import MenuPrincipalHandler
from Pantallas.CalcularImc import CalcularImcHandler
from Pantallas.Registrarme import RegistrarmeHandler
from Pantallas.Salir import SalirHandler

# CONFIGURACION DEPENDENCIAS
repo = RepositorioUsuarios()
repo.guardar(Usuario(Correo('correo@gmail.com'), Contraseña('contraseña')))

# CONFIGURACION PANTALLAS
imc = CalcularImcHandler()
registrarme = RegistrarmeHandler(repo)
salir = SalirHandler()

menu = MenuNavegacion() \
    .titulo('Menu Principal') \
    .agregarOpcion('Registrarme', registrarme) \
    .agregarOpcion('Salir', salir)

menuPrincipal = MenuPrincipalHandler(menu)

# NAVEGACION
registrarme.setNext(imc).setNext(menuPrincipal)

# INICIAR APLICACION
menuPrincipal.handle()
