Nombre = "Dilan"
Vida =100
Arma = "Arco y flecha"

print("Bienvenido a la aventura, " + Nombre + "!")
print(f"Tu vida es de {Vida} puntos.")
print("Tu arma es un " + Arma + ".")
print ("¡Prepárate para enfrentar peligros y desafíos en tu camino hacia la victoria!")

Inventario = [Nombre, Vida, Arma]
print(f"Tu inventario es: {Inventario}")

explorar = input("¿Quieres explorar el bosque? (s/n) ").lower()
if explorar == "s":
    print("¡Exploras el bosque y encuentras un enemigo!")
elif explorar == "n":
    print("Decides no explorar el bosque y te quedas en tu campamento.")
    exit()
else:
    print("Respuesta no valida. Por favor, elige una respuesta correcta s/n.")

for _ in range(1):
    enemigo = input("¡El enemigo esta cerca! ¿Qué tipo de enemigo es? ")
    print(f"¡Te enfrentas a un {enemigo}!")
    accion = input("¿Qué acción quieres tomar? (atacar, huir) ")
    if accion == "atacar":
        print(f"¡Atacas al {enemigo} con tu {Arma} y pierdes porque no tienes armadura!")
        Vida -=5 
        print(f"Perdiste 5 puntos de vida. Tu vida actual es: {Vida} puntos.")
    elif accion == "huir":
        print(f"¡Huyes del {enemigo} y te alejas del peligro!")
        print(input("¿Quieres explorar el bosque de nuevo? (s/n) ").lower())

def curar(Vida):
    Vida += 15
    return Vida
print("¡Encuentras una poción de curación!")
respuesta = input("¿Quieres tomar la poción de curación? (s/n) ").lower()
if respuesta == "s":
    print("¡Tomas la poción de curación y recuperas 15 puntos de vida!")    
elif respuesta == "n":
    print("Decides no tomar la poción de curación y sigues adelante.")
Vida = curar(Vida)
print(f"Tu vida actual es: {Vida} puntos.")
