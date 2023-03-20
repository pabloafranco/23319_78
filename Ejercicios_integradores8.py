"""
Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase
CuantaJoven que deriva de la clase creada en el punto 7. Cuando se crea esta nueva clase,
además del titular y la cantidad se debe guardar una bonificación que estará expresada en
tanto por ciento. Crear los siguientes métodos para la clase:
 Un constructor.
 Los setters y getters para el nuevo atributo.
 En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad, por lo
tanto hay que crear un método es_titular_valido() que devuelve verdadero si el titular es
mayor de edad pero menor de 25 años y falso en caso contrario.
 Además, la retirada de dinero sólo se podrá hacer si el titular es válido.
 El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la
cuenta.
"""
from Ejercicios_integradores7 import Cuenta

class CuentaJoven(Cuenta):
    def __init__(self, titular, edad, cantidad, bonificacion):
        super().__init__(titular, cantidad)
        self.__bonificacion = bonificacion
        self.__edad = edad

        #GETTER
    @property
    def bonificacion(self):
        return self.__bonificacion

    #SETTER
    @bonificacion.setter
    def bonificacion(self,nueva_bonificacion):
        try:
            self.__bonificacion = int(nueva_bonificacion)
        except:
            print (f'Valor incorrecto {nueva_bonificacion}')
        
    @property
    def edad(self):
        return self.__edad

    #SETTER
    @edad.setter
    def edad(self,nueva_edad):
        try:
            self.__edad = int(nueva_edad)
        except:
            print (f'Valor incorrecto {nueva_edad}')

    def es_titular_valido(self):
        return self.__edad >= 18 and self.__edad <= 25
    
    def retirar(self, cantidad ):
        if self.es_titular_valido():
            super.retirar(self, cantidad)
        else:
            print("No es un titular valido")

    def mostrar(self):
        super().mostrar()
        print(f'Cuenta Joven - Bonificacion de: {self.__bonificacion}%') 
     
nuevacuenta=CuentaJoven("Pablo", 30, 0, 10)
nuevacuenta.retirar(20)
nuevacuenta.mostrar()


