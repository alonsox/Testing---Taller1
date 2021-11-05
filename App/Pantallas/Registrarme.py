from typing import Any
from getpass import getpass
from Dominio.Apellido import Apellido
from Dominio.Edad import Edad
from Dominio.Nombre import Nombre
from Dominio.Sexo import Sexo
from Dominio.Usuario import Usuario
from Dominio.Correo import Correo
from Dominio.Contraseña import Contraseña
from Dominio.RepositorioUsuarios import RepositorioUsuarios
from Pantallas.Pantalla import Pantalla
from Utilidades.Otros import tryWhileError


class Registrarme(Pantalla):
    def __init__(self, repoUsuarios: RepositorioUsuarios) -> None:
        super().__init__()
        self._repoUsuarios = repoUsuarios

    def mostrar(self, data: Any = None) -> None:
        self.limpiar()
        print('REGISTRAR NUEVO USUARIO', end='\n\n')

        # LEER DATOS DEL USUARIO
        nombre = tryWhileError(lambda: Nombre(input('Nombre: ')))
        apellido = tryWhileError(lambda: Apellido(input('Apellido: ')))
        correo = tryWhileError(self._leerCorreo)
        sexo = tryWhileError(lambda: Sexo(input('Sexo: ')))
        edad = tryWhileError(lambda: Edad(input('Edad: ')))
        contraseña = tryWhileError(lambda: Contraseña(getpass("Contraseña: ")))

        # CREAR USUARIO
        usuario = Usuario(correo, contraseña, nombre, apellido, edad, sexo)

        # GUARDAR USUARIO
        try:
            self._repoUsuarios.guardar(usuario)
            print('Usuario creado correctamente')
            print('Presione enter para continuar...')
            self.navegar('menu_deslogueado', usuario)
        except:
            print('Hubo un error al crear el usuario.')
            print('Presione enter para volver al menu principal...')
            self.navegar('menu_deslogueado')

    def _leerCorreo(self) -> Correo:
        correo = Correo(input("Correo: "))
        if self._repoUsuarios.buscar(correo.valor()):
            raise Exception('El correo ya existe')
        else:
            return correo
