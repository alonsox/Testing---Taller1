import sys
from typing import Any
from Pantallas.Pantalla import Pantalla


class Salir(Pantalla):
    def mostrar(self, data: Any = None) -> None:
        print('Chao con vo loco, no estoy ni ahi')
        sys.exit(0)
