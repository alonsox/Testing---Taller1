from Pantallas.Registrarme import Registrarme
from Pantallas.Salir import Salir
from Dominio.RepositorioUsuariosCSV import RepositorioUsuariosCSV
from Pantallas.MenuDeslogueado import MenuDeslogueado
from Pantallas.CalcularImc import CalcularImc
from Pantallas.CalcularImc import CalcularImc
from Pantallas.MenuDeslogueado import MenuDeslogueado
from Pantallas.Registrarme import Registrarme
from Pantallas.Salir import Salir

# CONFIGURACION DEPENDENCIAS
repo = RepositorioUsuariosCSV('DB/usuarios.csv')

# CREAR PANTALLAS
imc = CalcularImc()
salir = Salir()
registrarme = Registrarme(repo)
menuDeslogueado = MenuDeslogueado()

# NAVEGACION
registrarme.navMenu() \
    .agregarRuta('imc', imc) \

imc.navMenu() \
    .agregarRuta('menu_deslogueado', menuDeslogueado) \

menuDeslogueado.navMenu() \
    .agregarRuta('registrarme', registrarme, 'Registrarme')\
    .agregarRuta('salir', salir, 'Salir') \

# INICIAR APLICACION
menuDeslogueado.mostrar()
