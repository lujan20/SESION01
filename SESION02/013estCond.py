#el programa si puede votar o no el usuario

nombre=input('Escribe tu nombre: ')
edad=int(input('Escribe tu edad por favor: '))
if(edad<=18):
 print(nombre,'No puedes votar')
else:
 print(nombre,'si puedes votar')

