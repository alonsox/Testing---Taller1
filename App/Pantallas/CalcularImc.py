from Pantallas.Pantalla import Pantalla
from Dominio.Usuario import Usuario
from Dominio.Altura import Altura
from Dominio.Peso import Peso
from Dominio.IMC import IMC
from Utilidades.Otros import tryWhileError


class CalcularImc(Pantalla):
    def mostrar(self, usuario: Usuario) -> None:
        self.limpiar()
        print(f'Calculando IMC para {str(usuario.nombre)}', end='\n\n')
        altura = tryWhileError(lambda:Altura(input("Altura: ")))
        peso = tryWhileError(lambda:Peso(input("Peso: ")))
        calculadoraIMC = IMC(altura,peso,usuario.sexo)
        print(f"Tu IMC es: {calculadoraIMC.calcularIMC()}")
        print(f"Tu estado es: {calculadoraIMC.evaluarIMC()}")

        input('Presiona enter para volver al menu principal...')
        self.navegar('menu_logueado', usuario)

    
