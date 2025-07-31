#LOGIN CON INTENTOS MAXIMOS
usuario="Sixto"
contrasena="1234"
intentos_maximos=3
for intentos in range (intentos_maximos):
    usuario_ing=input("ingrese su usuario: ")
    contra_ingre=input("ingrese su contraseña: ")
    if usuario_ing==usuario and contra_ingre==contrasena:
        print("Bienvenido al programa")
        break
    elif usuario_ing!=usuario:
        print("usuario incorrecto")
    elif contra_ingre!=contrasena:
        print("contraseña incorrecta")