from typing import Any
from Dominio.Usuario import Usuario
from Pantallas.Pantalla import Pantalla

class MenuLogueado(Pantalla):
    def mostrar(self, usuario: Usuario = None) -> None:
        self.limpiar()
        print(f'Bienvenido {str(usuario.nombre)}', end='\n\n')
        self.navMenu().descripcion('MENU LOGUEADO').mostrar(usuario)
