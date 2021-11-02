from typing import Union
from Dominio.ValueObject import ValueObject


class Edad(ValueObject[float]):
    def __init__(self, Edad: Union[int]) -> None:
        # VALIDAR QUE SEA UN NUMERO ENTERO
        if type(edad) != type(1) or type(edad) == type(1.1):
            raise Exception('La edad debe ser un número entero')

        # VALIDAR QUE SEA POSITIVO
        if edad < 15 or edad > 70:
            raise Exception('La edad debe estar entre 15 y 70 años')

        super().__init__(float(edad))
