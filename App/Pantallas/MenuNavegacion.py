from typing import Any, NamedTuple
from Pantallas.Mostrable import Mostrable


class OpcionNavegacion(NamedTuple):
    ruta: str
    mostrable: Mostrable
    mensajeMenu: str


class MenuNavegacion(Mostrable):
    def __init__(self) -> None:
        self._descripcion: str = 'Menu Navegación'
        self._opciones: list[OpcionNavegacion] = []

    def descripcion(self, des: str) -> 'MenuNavegacion':
        self._descripcion = des
        return self

    def agregarRuta(self, ruta: str, pantalla: Mostrable, mensajeMenu: str = '') -> 'MenuNavegacion':
        mensajeMenu = mensajeMenu if mensajeMenu else ruta
        self._opciones.append(OpcionNavegacion(ruta, pantalla, mensajeMenu))
        return self

    def navegar(self, ruta: str, data: Any = None) -> None:
        for opcion in self._opciones:
            if opcion.ruta == ruta:
                opcion.mostrable.mostrar(data)

    def mostrar(self, data: Any = None) -> None:
        # MOSTRAR OPCIONES
        print(self._descripcion, end='\n\n')
        for indice, opcion in enumerate(self._opciones):
            print("({0}) {1}".format(indice + 1, opcion.mensajeMenu))

        # OBTENER OPCION DEL USUARIO
        print('')
        opcion = -1
        while(True):
            try:
                opcion = int(input('> '))
                if (opcion < 1 or opcion > len(self._opciones)):
                    raise Exception('')
                else:
                    break
            except:
                print("Debe elegir un número entre entre 1 y {0}".format(
                    len(self._opciones)))

        # DEVOLVER EL HANDLER ASOCIADO A LA OPCION
        return self._opciones[opcion - 1].mostrable.mostrar()
