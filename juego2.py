#JUEGO DE PIEDRA PAPEL O TIJERA
#estamos usando el modulo para seleccionar una opcion random
import random
#estamos creando una lista con tres elementos
opciones=["piedra","papel","tijera"]
seguir="SI"
while seguir=="SI":
    elegir=input("ingrese su respuesta: ").lower()
    #validando que el usuario haya elegido una opcion que este
    #dentro de la lista
    if elegir in opciones:
        maquina=random.choice(opciones)
        if elegir==maquina:
            print(f"la computadora eligio {maquina} es un empate")
        elif elegir=="piedra" and maquina=="tijera" or elegir=="tijera" and maquina=="papel"or elegir=="papel" and maquina=="piedra":
            print(f"la computadora eligio {maquina} has ganado")
        else:
            print(f"la computadora eligio {maquina} has perdido")
        seguir=input("¿desea volver a jugar?: ").upper()
    else:
        print("opcion no valida")