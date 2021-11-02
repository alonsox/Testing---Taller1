from typing import Any
from getpass import getpass
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

        correo = tryWhileError(self._leerCorreo)
        contraseña = tryWhileError(lambda: Contraseña(getpass("Contraseña: ")))

        usuario = Usuario(correo, contraseña)

        self._repoUsuarios.guardar(usuario)
        self.navegar('imc', usuario)

    def _leerCorreo(self) -> Correo:
        correo = Correo(input("Correo: "))
        if self._repoUsuarios.buscar(correo.valor()):
            raise Exception('El correo ya existe')
        else:
            return correo
