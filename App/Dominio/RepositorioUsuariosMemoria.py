from typing import Union
from Dominio.RepositorioUsuarios import RepositorioUsuarios
from Dominio.Usuario import Usuario


class RepositorioUsuariosMemoria(RepositorioUsuarios):
    def __init__(self) -> None:
        self._usuarios: list[Usuario] = [] 

    def guardar(self, usuario: Usuario) -> None:
        # VERIFICA QUE EL CORREO NO ESTE EN USO
        if self.buscar(str(usuario.correo)):
            raise Exception(
                'El usuario con correo {0} ya existe'.format(usuario.correo))
        
        # GUARDA EL USUARIO
        self._usuarios.append(usuario)

    def buscar(self, correo: str) -> Union[Usuario, None]:
        for usuario in self._usuarios:
            if usuario.correo() == correo:
                return usuario
        else:
            return None