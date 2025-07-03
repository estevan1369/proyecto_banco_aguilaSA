historial=[]
saldo=0

print("bienvenido a banco aguila\n: por favor ingrese la carpeta")

contraseña=(input("ingrese la contraseña: "))
clave="ramon"

while True :
    contraseña=(input("retifique la contraseña: "))
    if clave ==clave: 
        print("¡conturaseña correcta!")
        break
    else:
        print("¡conturaseña incorrecta!")

print("1: consultar saldo\n 2:depositar\n 3:retirar\n 4:ver historial\n 5:salir\n 6:volver al menu")

def bloque_especifico():
    print("1: consultar saldo\n 2:depositar\n 3:retirar\n 4:ver historial\n 5:salir\n 6:volver al menu")
    

while True :
    usu=(int(input("ingrese una opcion(salir / volver): ")))
    if usu ==1:
        print(f"tu saldo actual es de :{saldo}")
    elif usu ==2:
        monto=(float(input("iingrese la contidad a depositar: ")))
        numcuenta=(int(input("ingrese el numero de cuenta: ")))
        saldo+=monto
        historial.append(f"+{monto} deposito")
        interes=monto*0.005
        print(f"se deposito en la cuenta, {numcuenta} : {monto} - {interes} + {saldo}")
    elif usu ==3:
        monto=(float(input("ingrese la cantidad a retirar: ")))
        numcuenta=(int(input("ingrese el numero de cuenta: ")))
        saldo-=monto
        historial.apppend(f"-{monto}retiro")
        print(f"se han retoirado{monto} en la cuenta {numcuenta}")
    elif usu ==4:
        print("historial de operaciones")
        for h in historial:
            print(h)
        print(f"el historial es {historial} y el saldo es {saldo}")
    elif usu=="salir":
        print("programa finalizado...")
        break
    elif usu =="volver":
        bloque_especifico()
    else:
        print("se produjo un error, gracias por utilizar banco aguila regrese en una hora")

    
