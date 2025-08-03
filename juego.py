#JUEGO DE PIEDRA PAPEL O TIJERA
#estamos usando el modulo para seleccionar una opcion random
import random
#estamos creando una lista con tres elementos
opciones=["piedra","papel","tijera"]
seguir="SI"
while seguir=="SI":
    error=False
    elegir=input("ingrese su respuesta: ").lower()
    if elegir not in  opciones:
            print("opcion no valida")
            error=True
            break
    if not error:
        maquina=random.choice(opciones)
        if elegir == maquina:
            print(f"la computadora eligio {maquina} es un empate")
        elif elegir =="piedra" and maquina =="tijera":
            print(f"la computadora eligio {maquina} has ganado")
        elif elegir =="tijera" and maquina =="papel":
            print(f"la computadora eligio {maquina} has ganado")
        elif elegir =="papel" and maquina =="piedra":
            print(f"la computadora eligio {maquina} has ganado")
        else:
            print(f"la computadora eligio {maquina} has perdido")
        seguir=input("¿desea volver a jugar?: ").upper()
        