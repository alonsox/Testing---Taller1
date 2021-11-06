import sys
from typing import Any
from Pantallas.Pantalla import Pantalla


class Salir(Pantalla):
    def mostrar(self, data: Any = None) -> None:
        print('Nos vemos pronto!!')
        sys.exit(0)
