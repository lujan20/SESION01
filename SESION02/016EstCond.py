#el programa pedira una cantidad en soles peruanos y mostrara un menu con opciones
#  para convertir a dolares y mexicanos
pesos=float(input('escribe la cantidad en pesos mexicanos: '))
opcion=float(input('\n A cual moneda deseas convertir: ' 
                   '\n 1. Dolares $17'
                   '\n 2. Soles $4\n'))
mensaje1='La cantidad convertida en Dolares es: '
mensaje2='La cantidad convertida en soles es: '
ancho=80

if(opcion==1):
    total=pesos/17
    mensaje1=mensaje1.center(ancho)
    print(mensaje1,round(total,2))
elif(opcion==2):
    total=pesos/4
    mensaje2=mensaje2.center(ancho)
    print(mensaje2,round(total,2))
else:
    print('Eligiste una opcion no validad')
