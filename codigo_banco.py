# 
import json
try:
    with open("datos.json", "r") as archivo:
        datos=json.load(archivo)
        saldo=datos["saldo"]
        historial=datos["historial"]
except FileNotFoundError:
    historial=[]
    saldo=0



#la lista se utiliza para guardar el histprial de todas las transacciones

 
 #se muestra el saldo actual del usuario


#imprimo un mensaje de bienvenida para el ususari 
print("bienvenido a banco aguila\n: por favor ingrese la tarjeta")

#solicito al usuario la contraseña (pero no la valida)
contraseña=(input("ingrese la contraseña: "))

#clave correcta
clave="ramon"

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
        print(f"se deposito en la cuenta, numero de cuenta : {numcuenta}\n  dinero depositado : {monto}\n menos el interes de '0,5%': {interes}\n totalidad ingresada en la cuenta: {monto_neto}\n el saldo actial : {saldo}\n")
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
        print(f"el historial es : {historial}\n  el saldo es : {saldo}\n")
        print("gracias por visitar el banco aguila")

        #esto finaliza el proigrama si el usuario ingresa salir, imprimiendo el menzaje (programa finalizado...)
    elif usu=="salir":
        print("programa finalizado...\n")
        print("gracias por visitar el banco aguila")

        with open("datos.json","w") as archivo:
            json.dump({"saldo":saldo,"historial":historial},archivo)
            break

    #llama la funcion 'def' la cual imprime nuevamente el menu
    elif usu =="volver":

        #permite que el usuario vea de nuevo el menu sin salir de programa y continuar ejecutar nuevas opciones 
        bloque_especifico()

        #si la opcion ingresada por el usuario no es ninguna de las validas (1 ,2 ,3 ,4 , "salir", "volver") imprime un mensaje indicando que se produjo un error 
    else:
        print("se produjo un error")
print("gracias porpreferir a nuestro banco S.A\n ¡que tenga buen dia!\n  Errrrr diablaz000")
    
