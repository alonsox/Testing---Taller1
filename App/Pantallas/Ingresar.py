from typing import Any
from getpass import getpass
from Dominio.RepositorioUsuarios import RepositorioUsuarios
from Pantallas.Pantalla import Pantalla


class Ingresar(Pantalla):
    def __init__(self, repoUsuarios: RepositorioUsuarios) -> None:
        super().__init__()
        self._repoUsuarios = repoUsuarios

    def mostrar(self, data: Any = None) -> None:
        self.limpiar()
        print('INGRESAR', end='\n\n')

        # LEER DATOS DE INGRESO
        correo = input("Correo: ")
        contraseña = getpass("Contraseña: ")

        # BUSCA EL USUARIO
        usuario = self._repoUsuarios.buscar(correo)

        # LOGIN
        if usuario and usuario.esContraseñaValida(contraseña):
            self.navegar('menu_logueado', usuario)
        else:
            print('\nDATOS DE INGRESO INVÁLIDOS', end='\n\n')
            input('Presione ENTER para volver al menú principal...')
            self.navegar('menu_deslogueado')
