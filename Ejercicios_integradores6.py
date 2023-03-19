"""
Crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construya los
siguientes métodos para la clase:
 Un constructor, donde los datos pueden estar vacíos.
 Los setters y getters para cada uno de los atributos. Hay que validar las entradas de
datos.
 mostrar(): Muestra los datos de la persona.
 Es_mayor_de_edad(): Devuelve un valor lógico indicando si es mayor de edad.

"""

class Persona:
    def __init__(self,codigo,nombre,edad,DNI):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__edad = edad
        self.__DNI = DNI

    def __str__(self) -> str:
        return f'Codigo: {self.codigo} \nNombre: {self.nombre} \nEdad:{self.edad} \nDNI: {self.DNI}'    
    
    #GETTER
    @property
    def codigo(self):
        return self.__codigo

    #SETTER
    @codigo.setter
    def nombre(self,nuevo_codigo):
        self.__codigo = nuevo_codigo


    #GETTER
    @property
    def nombre(self):
        return self.__nombre

    #SETTER
    @nombre.setter
    def nombre(self,nuevo_nombre):
        if len(nuevo_nombre)>3:
            self.__nombre = nuevo_nombre
        else:
            print ("Nombre Invalido, debe tener mas de 3 caracteres")

    #GETTER
    @property
    def edad(self):
        return self.__edad

    #SETTER
    @edad.setter
    def edad(self,nueva_edad):
        try:
            if not (int(nueva_edad)<=0 or int(nueva_edad)>=150):
                self.__edad = int(nueva_edad)
            else:
                print ("Edad Invalida, debe tener ser mayor que 0 y menor que 150 de 3 caracteres")
        except:
                print("Edad Invalida")
    
    #GETTER
    @property
    def DNI(self):
        return self.__DNI

    #SETTER
    @DNI.setter
    def DNI(self,nuevo_DNI):
        try:
            self.__DNI = int(nuevo_DNI)
        except:
            print("DNI Invalido")
    
    def mostrar(self) -> str:
        print(f'Codigo: {self.__codigo} - Nombre: {self.__nombre} - Edad:{self.__edad}  - DNI:{self.__DNI}')

    def Es_mayor_de_edad(self):
        return self.__edad >= 18



nueva_persona=Persona(1, "Pablo", 22, 17331208)
nueva_persona.mostrar()
print(nueva_persona)
print(nueva_persona.Es_mayor_de_edad())


nueva_persona2=Persona(2, "Sofia", 12, 47350167)
nueva_persona2.mostrar()
print(nueva_persona2.Es_mayor_de_edad())
"""

print (nueva_persona)

nueva_persona.edad=30
print(nueva_persona.edad)

nueva_persona.DNI=15265452
print(nueva_persona.DNI)
"""
