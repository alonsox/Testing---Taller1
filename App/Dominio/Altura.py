from typing import Union
from Dominio.ValueObject import ValueObject


class Altura(ValueObject[float]):
    def __init__(self, altura: Union[float,int,str]) -> None:
        # VALIDAR QUE SEA UN NUMERO
        if type(altura) == type(''):
            try:
                altura = float(altura)
            except:
                raise Exception('La altura debe ser un número')

        # VALIDAR QUE SEA UN NUMERO DECIMAL
        if type(altura) != type(1) and type(altura) != type(1.1):
            raise Exception('La altura debe ser un número')
        
        # VALIDAR QUE SEA POSITIVO
        if altura < 0:
            raise Exception('La altura no puede ser un número negativo')

        

        super().__init__(float(altura))
