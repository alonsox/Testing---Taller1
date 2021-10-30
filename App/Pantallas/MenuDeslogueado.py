from typing import Any
from Pantallas.Pantalla import Pantalla
from Utilidades.Otros import limpiarPantalla

class MenuDeslogueado(Pantalla):
    def mostrar(self, data: Any = None) -> None:
        limpiarPantalla()
        self.navMenu().descripcion('MENU DESLOGUEADO').mostrar()
