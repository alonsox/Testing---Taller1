from Pantallas.Pantalla import Pantalla
from Dominio.Usuario import Usuario
from Dominio.Altura import Altura
from Dominio.Peso import Peso
from Dominio.Edad import Edad


class CalcularImc(Pantalla):
    def mostrar(self, usuario: Usuario) -> None:
        self.limpiar()
        print('Calculando IMC para [' + usuario.correo() + ']', end='\n\n')
        input('Presiona enter para volver al menu principal...')
        self.navegar('menu_deslogueado')

    def _LeerAltura(self) -> Altura:
        altura = Altura(input("Altura: "))

    def _LeerPeso(self) -> Peso:
        peso = Peso(input("Peso: "))
