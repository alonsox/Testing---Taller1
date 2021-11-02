from Pantallas.Pantalla import Pantalla
from Dominio.Usuario import Usuario


class CalcularImc(Pantalla):
    def mostrar(self, usuario: Usuario) -> None:
        self.limpiar()
        print('Calculando IMC para [' + usuario.correo() + ']', end='\n\n')
        input('Presiona enter para volver al menu principal...')
        self.navegar('menu_deslogueado')
