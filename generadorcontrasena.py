#Generador de contraseña segura
import random
import string #es para poder generar letras numeros y simbolos
def generar_contraseña(longitud): #funcion para generar contraseña
    if longitud<10: #pedimos la longitud
        print("contraseña debil")
        return ""
    letras=string.ascii_letters
    numeros=string.digits
    simbolos=string.punctuation
    todo=letras+numeros+simbolos
    contraseña=[random.choice(letras),
                random.choice(numeros),
                random.choice(simbolos)]#una lista que almacena 3 tipos de elementos
    for _ in range(longitud-3):#restamos a la longitud total los tres elementos
        #que ya tenemos guardado en la lista contraseña 
        contraseña.append(random.choice(todo))#el .append sirve para abrir y editar 
        #elementos de mi lista
    random.shuffle(contraseña)#.shuffle sirve para mezclar mi string
    return ''.join(contraseña)
print("GENERADOR DE CONTRASEÑA")
while True:
    try:
        longitud=int(input("De cuantos caracteres quiere su contraseña: "))
        nuevacontraseña=generar_contraseña(longitud)
        if nuevacontraseña:
            print(f"su contraseña es:{nuevacontraseña}")
        otra=input("desea generar otra contraseña si/no: ").upper()
        if otra!="SI":
            break
    except: 
        print("porfavor ingresa un numero valido")