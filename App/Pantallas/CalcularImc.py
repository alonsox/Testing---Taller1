from Pantallas.Pantalla import Pantalla
from Dominio.Usuario import Usuario
from Dominio.Altura import Altura
from Dominio.Peso import Peso
from Dominio.IMC import IMC
from Utilidades.Otros import tryWhileError
from datetime import datetime


class CalcularImc(Pantalla):
    def mostrar(self, usuario: Usuario) -> None:
        self.limpiar()
        print(f'Calculando IMC para {str(usuario.nombre)}', end='\n\n')
        fecha_peso = tryWhileError(self._leerFecha)
        print(fecha_peso.strftime("%d/%m/%Y %H:%M"))
        altura = tryWhileError(lambda:Altura(input("Altura (Metros): ")))
        peso = tryWhileError(lambda:Peso(input("Peso (KG): ")))
        calculadoraIMC = IMC(altura,peso,usuario.sexo)
        self.limpiar()
        print(f"Tu índice de masa corporal es: {calculadoraIMC.calcularIMC()}")
        print(f"Tu estado es: {calculadoraIMC.evaluarIMC()}")

        input('Presiona enter para volver al menu principal...')
        self.navegar('menu_logueado', usuario)

    def _leerFecha(self):
        try: 
            my_string = str(input('Ingrese la fecha y hora del peso (dd/mm/yyyy hh:mm): '))
            return datetime.strptime(my_string, "%d/%m/%Y %H:%M")
        except:
            raise Exception('Ingrese la fecha en el formato correcto')
