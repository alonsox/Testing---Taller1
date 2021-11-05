from Pantallas.Ingresar import Ingresar
from Pantallas.Registrarme import Registrarme
from Pantallas.Salir import Salir
from Dominio.RepositorioUsuariosCSV import RepositorioUsuariosCSV
from Pantallas.MenuDeslogueado import MenuDeslogueado
from Pantallas.MenuLogueado import MenuLogueado
from Pantallas.CalcularImc import CalcularImc
from Pantallas.Registrarme import Registrarme
from Pantallas.Salir import Salir


# CONFIGURACION DEPENDENCIAS
repo = RepositorioUsuariosCSV('DB/usuarios.csv')

# CREAR PANTALLAS
imc = CalcularImc()
salir = Salir()
ingresar = Ingresar(repo)
registrarme = Registrarme(repo)
menuDeslogueado = MenuDeslogueado()
menuLogueado = MenuLogueado()

# NAVEGACION
ingresar.navMenu() \
    .agregarRuta('menu_logueado', menuLogueado) \

registrarme.navMenu() \
    .agregarRuta('menu_deslogueado', menuDeslogueado) \

imc.navMenu() \
    .agregarRuta('menu_logueado', menuLogueado) \

menuDeslogueado.navMenu() \
    .agregarRuta('ingresar', ingresar, 'Ingresar') \
    .agregarRuta('registrarme', registrarme, 'Registrarme') \
    .agregarRuta('salir', salir, 'Salir') \

menuLogueado.navMenu() \
    .agregarRuta('imc', imc, 'Calcular IMC') \
    .agregarRuta('salir', salir, 'Salir') \
    .agregarRuta('menu_deslogueado', menuDeslogueado, 'Log out') \

# INICIAR APLICACION
menuDeslogueado.mostrar()
