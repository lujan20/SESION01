#calcula el promedio del un curso de un alumno
print('el programa calcula el promedio de 3 calificaciones de un alumno')

nombre=input('Escribe tu nombre:')
mat=float(input('escribe tu calificacion de matematica: '))
fis=float(input('escribe tu calificacion de Fisica: '))
quim=float(input('escribe tu calificacion de Quimica: '))
promedio=(mat+fis+quim)/3

print(nombre,'Tu promedio es:',round(promedio,2))
#ahora debes avisar al estudiante si aprobado o no
#Usamos estructuras selectivas
if(promedio>=12):
 print('Felidades, estas aprobado')
else:
 print('Lo sentimos, estas reprobado')
