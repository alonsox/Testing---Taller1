import hashlib
from Dominio.ValueObject import ValueObject


class Contraseña(ValueObject[str]):
    largoMinimo = 8
    largoMaximo = 20

    def __init__(self, pwd: str) -> None:
        # VALIDA QUE NO ESTE VACIA
        if not pwd.strip():
            raise Exception('La contraseña no puede estar vacía')
        
        # VALIDAR QUE ES UNA CADENA
        if type(pwd) != type(''):
            raise Exception('La contraseña debe ser un string')

        # VALIDA QUE TENGA EL LARGO CORRECTO
        if (len(pwd) < Contraseña.largoMinimo or len(pwd) > Contraseña.largoMaximo):
            raise Exception('La contraseña debe tener entre {0} y {1} caracteres'.format(
                Contraseña.largoMinimo, Contraseña.largoMaximo))

        super().__init__(self._hashear(pwd))

    def _hashear(self, pwd: str) -> str:
        # Fuente para hashear: https://recursospython.com/guias-y-manuales/hashlib-md5-sha/
        return hashlib.sha256(pwd.encode('utf-8')).hexdigest()

    def validar(self, pwdCandidata: str):
        return self._hashear(pwdCandidata) == self.valor()
