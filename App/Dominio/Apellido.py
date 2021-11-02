import re
from Dominio.ValueObject import ValueObject

class Apellido(ValueObject[str]):
    def __init__(self, nombre: str) -> None:
        # VALIDAR QUE ES UNA CADENA
        if type(apellido) != type(''):
            raise Exception('El nombre debe ser un string')

        # VALIDAR QUE EL CORREO NO ESTA VACÍO
        if not apellido.strip():
            raise Exception('El nombre no puede estar vacío')

        super().__init__(apellido)
