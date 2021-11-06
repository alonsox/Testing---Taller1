from typing import Any
from Dominio.Usuario import Usuario
from Pantallas.Pantalla import Pantalla

class MenuLogueado(Pantalla):
    def mostrar(self, usuario: Usuario = None) -> None:
        self.limpiar()
        bienvenide = 'Bienvenida' if usuario.sexo.esFemenino() else 'Bienvenido'
        mensajeMenu = f"{bienvenide} de vuelta {usuario.nombreCompleto()}"
        self.navMenu().descripcion(mensajeMenu).mostrar(usuario)
        
