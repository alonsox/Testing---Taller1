from typing import Union
from Dominio.Usuario import Usuario


class RepositorioUsuarios:
    def __init__(self) -> None:
        self._usuarios: list[Usuario] = [] 

    def guardar(self, usuario: Usuario) -> None:
        self._usuarios.append(usuario)

    def buscar(self, correo: str) -> Union[Usuario, None]:
        for usuario in self._usuarios:
            if usuario.correo() == correo:
                return usuario
        else:
            return None