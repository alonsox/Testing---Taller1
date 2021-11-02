import re
from Dominio.ValueObject import ValueObject

class Sexo(ValueObject[str]):
    def __init__(self, sexo: str) -> None:
        # VALIDAR QUE ES UNA CADENA
        if type(sexo) != type(''):
            raise Exception('El sexo debe ser un string')

        # VALIDAR QUE EL SEXO ESTE EN FORMATO (F/M)
        if sexo != 'F' or sexo != 'M':
            raise Exception('El sexo debe indicarse como Femenino o Masculino en formato F o M respectivamente')

        super().__init__(sexo)
