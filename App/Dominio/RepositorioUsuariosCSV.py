from typing import Union
from Dominio.RepositorioUsuarios import RepositorioUsuarios
from Dominio.Usuario import Usuario


class RepositorioUsuariosCSV(RepositorioUsuarios):
    def __init__(self) -> None:
        pass 

    def guardar(self, usuario: Usuario) -> None:
        pass

    def buscar(self, correo: str) -> Union[Usuario, None]:
        pass