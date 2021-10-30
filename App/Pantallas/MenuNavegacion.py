from typing import Any
from Pantallas.Mostrable import Mostrable

class OpcionNavegacion:
    def __init__(self, ruta: str, mensaje: str, mostrable: Mostrable) -> None:
        self.ruta: str = ruta
        self.mensaje: str = mensaje
        self.mostrable: Mostrable = mostrable

class MenuNavegacion(Mostrable):
    def __init__(self) -> None:
        self._descripcion: str = 'Menu Navegación'
        self._opciones: list[OpcionNavegacion] = []

    def descripcion(self, des: str) -> 'MenuNavegacion':
        self._descripcion = des
        return self

    def agregar(self, ruta: str, pantalla: Mostrable, mensaje: str = '') -> 'MenuNavegacion':
        mensaje = mensaje if mensaje else ruta
        self._opciones.append(OpcionNavegacion(ruta, mensaje, pantalla))
        return self

    def navegar(self, ruta: str, data: Any = None) -> None:
        for opcion in self._opciones:
            if opcion.ruta == ruta:
                opcion.mostrable.mostrar(data)

    def mostrar(self, data:Any = None) -> None:
        # MOSTRAR OPCIONES
        print(self._descripcion, end='\n\n')
        for indice, opcion in enumerate(self._opciones):
            print("({0}) {1}".format(indice + 1, opcion.mensaje))

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
