from typing import Any
from Pantallas.Pantalla import Pantalla

class MenuDeslogueado(Pantalla):
    def mostrar(self, data: Any = None) -> None:
        self.limpiar()
        self.navMenu().descripcion('Bienvenido al calculador de IMC').mostrar()
