from typing import Any
from Utilidades.Otros import limpiarPantalla
from Pantallas.MenuNavegacion import MenuNavegacion
from Pantallas.Mostrable import Mostrable


class Pantalla(Mostrable):
    def __init__(self) -> None:
        self._menuNavegacion: MenuNavegacion = MenuNavegacion()

    def navMenu(self) -> MenuNavegacion:
        return self._menuNavegacion

    def navegar(self, ruta, data: Any = None) -> None:
        self._menuNavegacion.navegar(ruta, data)

    def limpiar(self) -> None:
        limpiarPantalla()

    def mostrar(self, data: Any = None) -> None:
        pass
