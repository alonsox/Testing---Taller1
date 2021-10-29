from Pantallas.PantallaHandler import PantallaHandler
from Utilidades.Otros import limpiarPantalla


class OpcionMenu:
    def __init__(self, mensaje: str, handler: PantallaHandler):
        self.mensaje = mensaje
        self.handler = handler


class MenuNavegacion:
    def __init__(self) -> None:
        self._titulo: str = 'Menu'
        self._opciones: list[OpcionMenu] = []

    def titulo(self, titulo: str) -> 'MenuNavegacion':
        self._titulo = titulo
        return self

    def agregarOpcion(self, mensaje: str, handler: PantallaHandler) -> 'MenuNavegacion':
        self._opciones.append(OpcionMenu(mensaje, handler))
        return self

    def mostrar(self) -> PantallaHandler:
        # MOSTRAR OPCIONES
        limpiarPantalla()
        print(self._titulo, end='\n\n')
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
        return self._opciones[opcion - 1].handler
