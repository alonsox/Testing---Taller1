import re
from Dominio.ValueObject import ValueObject

class Correo(ValueObject[str]):
    def __init__(self, correo: str) -> None:
        # VALIDAR QUE ES UNA CADENA
        if type(correo) != type(''):
            raise Exception('El correo debe ser un string')

        # VALIDAR QUE EL CORREO NO ESTA VACÍO
        if not correo.strip():
            raise Exception('El correo no puede estar vacío')
    
        # VALIDAR QUE TENGA EL FORMATO CORRECTO
        # Fuente: https://parzibyte.me/blog/2018/12/04/comprobar-correo-electronico-python/
        regexCorreo = r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"
        if not re.match(regexCorreo, correo):
            raise Exception('El correo tiene un formato inválido')

        super().__init__(correo)
