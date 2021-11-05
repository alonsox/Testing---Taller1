from typing import Any
from Pantallas.Pantalla import Pantalla

class MenuIngresar(Pantalla):
    def mostrar(self, data: Any = None) -> None:
        self.limpiar()
        print('Ingresar nombre')
