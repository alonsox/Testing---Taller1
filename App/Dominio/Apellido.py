import re
from Dominio.ValueObject import ValueObject

class Apellido(ValueObject[str]):
    def __init__(self, apellido: str) -> None:
        # VALIDAR QUE ES UNA CADENA
        if type(apellido) != type(''):
            raise Exception('El apellido debe ser un string')

        # VALIDAR QUE EL APELLIDO NO ESTA VACÍO
        if not apellido.strip():
            raise Exception('El apellido no puede estar vacío')

        super().__init__(apellido)
