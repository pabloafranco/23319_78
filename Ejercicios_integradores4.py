"""
Escribir una función que reciba una cadena de caracteres y devuelva un diccionario con cada
palabra que contiene y la cantidad de veces que aparece (frecuencia). Escribir otra función
que reciba el diccionario generado con la función anterior y devuelva una tupla con la
palabra más repetida y su frecuencia.
"""

from Ejercicios_integradores3 import crearDiccionario

dicciona = crearDiccionario("Esto es una prueba de muchas cosas de todas las pruebas que esto todas de hicimos esto es lo mejor de todas las pruebas")

sorted_dicciona = dict(sorted(dicciona.items(), key=lambda item:item[1], 
reverse=True))
print(sorted_dicciona)

for key, value in sorted_dicciona.items():
  una_tupla=(key, value, )
  break


print (una_tupla)