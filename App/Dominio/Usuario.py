from Dominio.Contraseña import Contraseña
from Dominio.Correo import Correo
from Dominio.Nombre import Nombre
from Dominio.Apellido import Apellido
from Dominio.Edad import Edad
from Dominio.Sexo import Sexo


class Usuario:
    def __init__(self,
                 correo: Correo,
                 contraseña: Contraseña,
                 nombre: Nombre,
                 apellido: Apellido,
                 edad: Edad,
                 sexo: Sexo,
                 ) -> None:
        self.correo = correo
        self._contraseña = contraseña
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.sexo = sexo

    def esContraseñaValida(self, pwd: str) -> bool:
        return self._contraseña.validar(pwd)

    def nombreCompleto(self) -> str:
        return f"{self.nombre} {self.apellido}"

    def of(correo: str,
           contraseña: str,
           nombre: str,
           apellido: str,
           edad: int,
           sexo: str,
           ) -> 'Usuario':
        """
        Crea un nuevo usuario desde tipos base.

        NOTA: Usar este método solo para reconstituir usuarios desde un almacenamiento
        como un archivo CSV.
        """
        return Usuario(
            Correo(correo),
            Contraseña(contraseña, raw=True),
            Nombre(nombre),
            Apellido(apellido),
            Edad(edad),
            Sexo(sexo)
        )
