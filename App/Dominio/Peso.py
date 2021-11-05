from typing import Union
from Dominio.ValueObject import ValueObject


class Peso(ValueObject[float]):
    def __init__(self, peso: Union[float, int,str]) -> None:

        # VALIDAR QUE SEA UN NUMERO
        if type(peso) == type(''):
            try:
                peso = float(peso)
            except:
                raise Exception('El peso debe ser un número')

        # VALIDAR QUE SEA UN NUMERO DECIMAL
        if type(peso) != type(1) and type(peso) != type(1.1):
            raise Exception('El peso debe ser un número')

        # VALIDAR QUE SEA POSITIVO
        if peso < 0:
            raise Exception('El peso no puede ser un número negativo')

        super().__init__(float(peso))
