from Dominio.Altura import Altura
from Dominio.Peso import Peso
from Dominio.Sexo import Sexo

class IMC:
    def __init__(self, altura: Altura, peso: Peso, sexo: Sexo) -> None:
        # CALCULA IMC

        self._altura = altura
        self._peso = peso
        self._sexo = sexo
        
    
    def calcularIMC(self):
        return round(self._peso.valor()/self._altura.valor()**2,1)

    def evaluarIMC(self):
         
        valor_imc = self.calcularIMC()

        if self._sexo.esFemenino():
            if valor_imc < 20:
                return 'Bajo peso'
            elif valor_imc > 20 and valor_imc <= 23.9:
                return 'Normal'
            elif valor_imc > 23.9 and valor_imc <= 28.9:
                return 'Obesidad leve'
            elif valor_imc > 28.9 and valor_imc <= 37:
                return 'Obesidad severa'
            else:
                return 'Obesidad muy severa'

        if self._sexo.esMasculino():
            if valor_imc < 20:
                return 'Bajo peso'
            elif valor_imc > 20 and valor_imc <= 24.9:
                return 'Normal'
            elif valor_imc > 24.9 and valor_imc <= 29.9:
                return 'Obesidad leve'
            elif valor_imc > 29.9 and valor_imc <= 40:
                return 'Obesidad severa'
            else:
                return 'Obesidad muy severa'
 


