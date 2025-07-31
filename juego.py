import random
objeto=["piedra","papel","tijera"]
opcion=input("ingrese su opcion: ")
maquina=random.choice(objeto)
if opcion=="piedra" and maquina=="tijera":
    print(f"la maquina eligio {maquina} has ganado!!" )
elif opcion=="tijera" and maquina=="papel":
    print(f"la maquina eligio {maquina} has ganado!!" )
elif opcion=="papel" and maquina=="piedra":
    print(f"la maquina eligio {maquina} has ganado!!" )
elif opcion==maquina:
    print(f"la maquina eligio {maquina} empate" )
else:
    print(f"la maquina eligio {maquina} has perdido" )
