# el programa se basa en un codigo que simula la interaccion con un cajero automatico pide retirtar dinero, consultar saldo, depositar dinero, ver historial y sqlir. 

#JSON es un un formato de texto ligero para almacenar e intercanviar datos 
#este import funciona para incluir la biblioteca (json), que permite trabajar con datos en formato Json
import json

#aqui lee el contenido del archivo de datos. JSON lo convierte en un diccionario y luego se extraen, las claves, saldo y historial
try:
    with open("datos.json", "r") as archivo:

        #este especificamente lo convieryte en un diccionario
        datos=json.load(archivo)

        #extraeel saldo almacenado en el archivo y lo guarda en la variable saldo
        saldo=datos["saldo"]

        #extrae el historial de operaciones y lo guareda en la lista historial 
        historial=datos["historial"]
        
        #esto funciona para atrapar un error si el archivo no existe. si existe funciona normal; si no lanza un error FileNotFoundError
except FileNotFoundError:
    historial=[]
    saldo=0

 #se muestra el saldo actual del usuario
#imprimo un mensaje de bienvenida para el ususari 
print("bienvenido a banco aguila\n: por favor ingrese la tarjeta")

#solicito al usuario la contraseña (pero no la valida)
contraseña=(input("ingrese la contraseña: "))

#clave correcta
clave="jeremiaz69"

#inicio un bucle para balidar la contraseña hasta que sea correcta
while True :
    contraseña=(input("retifique la contraseña: "))
    if contraseña ==clave: 

        #comparo la contraseña ingresada con la clave correcta 
        print("¡contraseña correcta!")
        break
    else:
        print("¡conturaseña incorrecta!")

#muestro el menu principal 
print(" menu\n 1: consultar saldo\n 2:depositar\n 3:retirar\n 4:ver historial\n 5:salir\n 6:volver al menu")

#para que sirve "def" se utiliza para definir una funcion, en mi caso lo utilice para volver a ejecutar el codigo apartir de aqui solo si se cumple la condicion de (6 o volver)
#defini una variable para imprimir el menu (se utiliza cuando el usuario escribe 'salir' )
def bloque_especifico():
    print("1: consultar saldo\n 2:depositar\n 3:retirar\n 4:ver historial\n 5:salir\n 6:volver al menu")
    
#iniciamos el bucle principal del programa
while True :

    #se le pide al usñuañrio una opcion 
    usu=(input("ingrese una opcion(salir / volver): "))

    #si la opcion es un numero valido, lo convierte en entero
    if usu.isdigit():
        usu = int(usu)
    if usu ==1:

        #muestra al usuario el saldo actual disponible en su cuenta
        print(f"tu saldo actual es de :{saldo}\n")
        print("gracias por visitar el banco aguila")
    elif usu ==2:

        #solicito al usuario el monto a depositar y el numero de cuenta
        print("aviso:NO SE PUEDE DEPOSITAR MODOS NEGATIVOS O NO NUMERICOS")
        monto=(int(input("ingrese la contidad a depositar: ")))
        numcuenta=(int(input("ingrese el numero de cuenta: ")))
        

         #calculo un pequeño interes sobre el monto (0,5%)
        interes=monto*0.005

        #realizo una operacion para restar el interes al monto
        monto_neto=monto-interes

        #sumo el monto al saldo actual
        saldo+=monto_neto

        #registro la operacion en la lista 
        historial.append(f"+{monto_neto} deposito")

        #muestro un mensaje indicando el numero d cuenta, monto depositado, interes, monto total y el saldo actual
        print(f"se deposito en la cuenta, numero de cuenta : {numcuenta}\n dinero depositado : {monto}\n menos el interes de '0,5%': {interes}\n totalidad ingresada en la cuenta: {monto_neto}\n el saldo actial : {saldo}\n")
        print("gracias por visitar el banco aguila")
    elif usu ==3:

        #solicito el monto a depositar y el numero de cuenta
        monto=(int(input("ingrese la cantidad a retirar: ")))
        numcuenta=(int(input("ingrese el numero de cuenta: ")))

        #resto el monto retirdo al monto actual 
        saldo-=monto

        #registro la operacion en la lista
        historial.append(f"-{monto}retiro")

        #muestro un menu que indica el monto a retirar y el numero de cuenta
        print(f"se han retirado {monto} \n en la cuenta {numcuenta}\n")
        print("gracias por visitar el banco aguila")
    elif usu ==4:

        #imprimo un encabezado
        print("historial de operaciones")

        #esto recorre la lista e imprime cada operacion 
        for h in historial:
            print(h)

            #imprimo el historial y el saldo actual
        print(f"el historial es : {historial}\n el saldo es : {saldo}\n")
        print("gracias por visitar el banco aguila")

        #esto finaliza el proigrama si el usuario ingresa salir, imprimiendo el menzaje (programa finalizado...)
    elif usu=="salir":
        print("programa finalizado...\n")
        print("gracias por visitar el banco aguila")

#guardamos los datos antes de salir,saldo y historia y lo guarda en la variable archivo.
        with open("datos.json","w") as archivo:

            #lee el contenido del archivo Json y lo convierte en un diccionario de python 
            json.dump({"saldo":saldo,"historial":historial},archivo)
            break

    #llama la funcion 'def' la cual imprime nuevamente el menu
    elif usu =="volver":

        #permite que el usuario vea de nuevo el menu sin salir de programa y continuar ejecutar nuevas opciones 
        bloque_especifico()

        #si la opcion ingresada por el usuario no es ninguna de las validas (1 ,2 ,3 ,4 , "salir", "volver") imprime un mensaje indicando que se produjo un error 
    else:
        print("gracias porpreferir a nuestro banco S.A\n ¡que tenga buen dia!\n Errrrr diablaz000")
    
