from typing import Any
from Pantallas.Pantalla import Pantalla

class Ingresar(Pantalla):
    def mostrar(self, data: Any = None) -> None:
        self.limpiar()
        print('Ingresar nombre')
