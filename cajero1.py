#Funcionalidad de un cajero Automatico
#1. ver saldo actual
#2. depositar
#3. retiro
fondos=8000
intento=0
nip_correcto="1234"
print("--Bienvenido al cajero--")
#Autenticacion Simple
while intento<3:
    nip=input("ingrese su nip: ")
    if nip==nip_correcto:
        break
    else:
        print("nip incorrecto")
        intento +=1
if intento==3: #si se han realizado demasiados intestos se bolquea la tarjeta
    print("demasiados intentos. La tarjeta se ha bloqueado")
else: # de lo contrario entra al ciclo while
    while True: #siempre se cumple la condicion
        print("---MENU---")
        print("1. Ver saldo actual")
        print("2. Depositar")
        print("3. Retirar")
        print("4. Salir")
        opcion=input("Ingrese la operacion que desea realizar: ")# espera la opcion del usuario
        match opcion:
            case "1":
                print(f"su saldo es de {fondos}")# solo nos imprime nuestro saldo actual
            case "2":
                try:# para manejar errores
                    deposito=float(input("ingrese la cantidad a depositar: "))
                    if deposito>0:
                        fondos+=deposito #actaulizamos nuetra variable
                        print(f"Deposito de {deposito} exitoso. Nuevo saldo {fondos} ")
                    else:
                        print("monto no valido")
                except:# permite que nuestro no se rompa
                    print("entrada no valida")
            case "3":
                try:# para manejar errores
                    retirar=float(input("ingrese la cantidad a retirar: "))
                    if 0 < retirar<=fondos:#validamos que el usuario ingrese 
                        #una cantidad mayor a 0 y menor a la que hay en fondo
                        fondos-=retirar
                        print(f"retiro de {retirar} exitoso. Nuevo saldo {fondos}")
                    else:
                        print("fondos insuficietes")
                except:# permite que nuestro no se rompa
                    print("entrada no valida")
            case "4":
                break
            case _: #esto es por si no se ingresa una opcion del menu
                print("opcion no valida intente de nuevo")