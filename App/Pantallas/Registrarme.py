from getpass import getpass
from typing import Any
from Dominio.Usuario import Usuario
from Dominio.Correo import Correo
from Dominio.Contraseña import Contraseña
from Dominio.RepositorioUsuarios import RepositorioUsuarios
from Pantallas.PantallaHandler import PantallaHandler
from Utilidades.Otros import limpiarPantalla, tryWhileError


class RegistrarmeHandler(PantallaHandler):
    def __init__(self, repoUsuarios: RepositorioUsuarios) -> None:
        super().__init__()
        self._repoUsuarios = repoUsuarios

    def handle(self, data: Any = None) -> None:
        limpiarPantalla()
        print('REGISTRAR NUEVO USUARIO', end='\n\n')

        correo = tryWhileError(self._leerCorreo)
        contraseña = tryWhileError(lambda: Contraseña(getpass("Contraseña: ")))

        usuario = Usuario(correo, contraseña)

        self._repoUsuarios.guardar(usuario)
        self.next(usuario)

    def _leerCorreo(self) -> Correo:
        correo = Correo(input("Correo: "))
        if self._repoUsuarios.buscar(correo.valor()):
            raise Exception('El correo ya existe')
        else:
            return correo
