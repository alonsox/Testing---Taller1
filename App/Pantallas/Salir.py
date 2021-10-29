import sys
from typing import Any
from Pantallas.PantallaHandler import PantallaHandler

class SalirHandler(PantallaHandler):
    def handle(self, data: Any = None) -> None:
        print('Chao con vo loco, no estoy ni ahi')
        sys.exit(0)



