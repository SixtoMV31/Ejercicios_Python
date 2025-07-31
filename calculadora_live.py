print("Calculadora:")
print("1.Suma --2.resta --" \
"3.multiplicacion ---4.Division")
hacer=0
while hacer !=6:
    try:
        opcion=int(input("selecione la operacion:"))
        if opcion==1:
            print("<<<<Selecciono suma>>>>")
            num1=int(input("ingrese el primer numero: "))
            num2=int(input("Ingrese el segundo numero: "))
            print("el resultado es= ",num1+num2)
        elif opcion==2:
            print("<<<<Selecciono Resta>>>>")
            num1=int(input("ingrese el primer numero: "))
            num2=int(input("Ingrese el segundo numero: "))
            print("el resultado es= ",num1-num2)
        elif opcion==3:
            print("<<<<Selecciono Multuplicacion>>>>")
            num1=int(input("ingrese el primer numero: "))
            num2=int(input("Ingrese el segundo numero: "))
            print("el resultado es= ",num1*num2)
        elif opcion==4:
            print("<<<<Selecciono division>>>>")
            num1=int(input("ingrese el primer numero: "))
            num2=int(input("Ingrese el segundo numero: "))
            print("el resultado es= ",num1/num2)
        hacer=int(input("Seleccione 6 si desea terminar " \
    "el programa y 5 si desea hacer otra operacion: "))
    except:
            print("porfavor ingrese un dato valido")
    
print("gracias por usar la calculadora......")

