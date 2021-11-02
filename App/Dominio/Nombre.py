from Dominio.ValueObject import ValueObject

class Nombre(ValueObject[str]):
    def __init__(self, nombre: str) -> None:
        # VALIDAR QUE ES UNA CADENA
        if type(nombre) != type(''):
            raise Exception('El nombre debe ser un string')

        # VALIDAR QUE EL NOMBRE NO ESTA VACÍO
        if not nombre.strip():
            raise Exception('El nombre no puede estar vacío')
        
        # VALIDAR LARGO MAXIMO
        if len(nombre) > 100:
            raise Exception('El nombre no debe superar los 100 caracteres')

        super().__init__(nombre)
