import random
import time

limite_segundos = 120
inicio = time.time()

palabras = ("futbol", "dilan", "python", "computador", "iphone")
palabra_secreta = random.choice(palabras)
letras_adivinadas = []
vidas = 3 

print("=== AHORACADO ===")

print("Bienvenido al juego del ahorcado")

while vidas > 0:
    mensaje = ""
    for letra in palabra_secreta: 
        if letra in letras_adivinadas:
            mensaje += letra
        else:
            mensaje += "_"
    tiempo_transcurrido = int(time.time() - inicio)
    tiempo_restante = limite_segundos - tiempo_transcurrido
    print("Tiempo restante:", tiempo_restante, "segundos") 
    print(f"Palabra actual: {mensaje}")

    if "_" not in mensaje:
        print("¡Felicidades! Has adivinado la palabra secreta.")
        break

    print(f"Te quedan {vidas} vidas.")

    intento = input("Ingresa una letra: ").lower()

    if intento in letras_adivinadas:
        print("Ya has adivinado esa letra. Intenta con otra.")
    elif intento in palabra_secreta.lower():
        print("¡Correcto! Has adivinado una letra.")
        letras_adivinadas.append(intento)
    
    elif tiempo_restante <= 0:
        print("¡Tiempo agotado! Has perdido el juego.")
        break

    else:
        print("¡Incorrecto! Esa letra no está en la palabra secreta, intenta de nuevo.")
        letras_adivinadas.append(intento)
        vidas -= 1