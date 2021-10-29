from typing import Any
from Pantallas.PantallaHandler import PantallaHandler
from Pantallas.MenuNavegacion import MenuNavegacion


class MenuPrincipalHandler(PantallaHandler):
    def __init__(self, menu: MenuNavegacion) -> None:
        self._menu = menu

    def handle(self, data: Any = None) -> None:
        handler = self._menu.mostrar()
        handler.handle()
