#saber si es mayor de edad o adolecente
edad=int(input("edad: "))
if edad<12:
    print("es un niño")
elif edad <18:
    print("es un adolecente")
else:
    print("es mayor de edad")
