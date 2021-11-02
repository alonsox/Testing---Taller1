from Dominio.ValueObject import ValueObject

class Sexo(ValueObject[str]):
    def __init__(self, sexo: str) -> None:
        # VALIDAR QUE ES UNA CADENA
        if type(sexo) != type(''):
            raise Exception('El sexo debe ser un string')

        # VALIDAR QUE EL SEXO ESTE EN FORMATO (F/M)
        if (sexo.upper()) != 'F' and (sexo.upper()) != 'M':
            raise Exception('El sexo debe indicarse como Femenino o Masculino en formato F o M respectivamente')

        super().__init__(sexo.upper())
 
    def esFemenino(self) -> bool:
        return self.valor() == 'F'

    def esMasculino(self) -> bool:
        return self.valor() == 'M'