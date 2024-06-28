#el programa evaluara la estatura de un usuario
#si la estatura mide 160 cm imprimira: eres chato
#si la estatura mide 160 y 175 imprimira: eres de estatura mediano
#si la estatura mide mayor a 175 cm imprimira: eres alto
#

nombre=input('Escribe tu nombre: ')
edad=int(input('Escribe tu edad por favor: '))
altura=int(input('ingresa tu talla en centimetros: '))
if altura<160:
 print(nombre,'Eres chato')
if altura>=160 and altura<=175:
 print(nombre,'Eres de estatura mediando')
if altura>175:
 print(nombre,'Eres alto')