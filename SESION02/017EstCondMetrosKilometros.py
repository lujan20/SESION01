#convertir de metros a kilometros o a centimetros segun loq ue solicite el usuario
distancia=float(input('Escribe la cantidad en metros: '))
opcion=float(input('\n A que unidades deseas convertir: ' 
                   '\n a. converir en kilometros'
                   '\n b. converir en centimetros \n'))
mensaje1='La cantidad convertida a kilomentros es: '
mensaje2='La cantidad convertida en centimetros  es: '
ancho=80

if(opcion=='a'):
    total=distancia/1000
    mensaje1=mensaje1.center(ancho)
    print(mensaje1,opcion)
elif(opcion=='b'):
    total=distancia*100
    mensaje2=mensaje2.center(ancho)
    print(mensaje2,opcion)
else:
    print('Eligiste una opcion no validad')