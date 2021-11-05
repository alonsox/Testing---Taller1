from Pantallas.Registrarme import Registrarme
from Pantallas.Salir import Salir
from Dominio.RepositorioUsuariosCSV import RepositorioUsuariosCSV
from Pantallas.MenuDeslogueado import MenuDeslogueado
from Pantallas.MenuLogueado import MenuLogueado
from Pantallas.CalcularImc import CalcularImc
from Pantallas.Registrarme import Registrarme
from Pantallas.Salir import Salir
from Dominio.Apellido import Apellido
from Dominio.Edad import Edad
from Dominio.Nombre import Nombre
from Dominio.Sexo import Sexo
from Dominio.Usuario import Usuario
from Dominio.Correo import Correo
from Dominio.Contraseña import Contraseña

# CONFIGURACION DEPENDENCIAS
repo = RepositorioUsuariosCSV('DB/usuarios.csv')

# CREAR PANTALLAS
imc = CalcularImc()
salir = Salir()
registrarme = Registrarme(repo)
menuDeslogueado = MenuDeslogueado()
menuLogueado = MenuLogueado()

# NAVEGACION
registrarme.navMenu() \
    .agregarRuta('imc', imc) \

imc.navMenu() \
    .agregarRuta('menu_logueado', menuLogueado) \

menuDeslogueado.navMenu() \
    .agregarRuta('registrarme', registrarme, 'Registrarme')\
    .agregarRuta('salir', salir, 'Salir') \

menuLogueado.navMenu() \
    .agregarRuta('imc', imc, 'Calcular IMC')\
    .agregarRuta('salir', salir, 'Salir') \
    .agregarRuta('menu_deslogueado', menuDeslogueado, 'Log out')\

# INICIAR APLICACION
usuario = Usuario(Correo('a@a.a'), Contraseña('12345678'), Nombre('Nombre'), Apellido('Apellido'), Edad(20), Sexo('F') )
imc.mostrar(usuario)
