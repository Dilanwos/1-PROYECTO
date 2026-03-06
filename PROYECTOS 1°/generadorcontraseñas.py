print("=== GENERADOR DE CONTRASEÑAS ===") 
# 1 Importamos la libreria que tiene letras, numeros y simbolos
import string
# 3 importamos la libreria para generar valores aleatorios seguros
import secrets
# 2 Creamos variables para cada tipo de caracter
minusculas = string.ascii_lowercase
mayusculas = string.ascii_uppercase
numeros = string.digits
simbolos = string.punctuation
# 4 Pedimos al usuario que elija la fuerza de la contraseña
strength = input("Elige la fuerza de la contraseña (baja, media, alta): ").lower() 
if strength == "baja":
        caracteres = minusculas
elif strength == "media":
        caracteres = minusculas + mayusculas + numeros
elif strength == "alta":
        caracteres = minusculas + mayusculas + numeros + simbolos
else:
        print("Fuerza no valida. Por favor, elige una fuerza correcta.")
    
# 5 Pedimos al usuario que elija la longitud de la contraseña
length = int(input("Elige la longitud de la contraseña (8, 12, 16): "))
if length in [8, 12, 16]:
    pass
else:
    print("Longitud no valida. Por favor, elige una longitud correcta.")
caracteres = "" 
while True:
    resp_minus = input("¿Deseas incluir letras minusculas? (s/n): ").lower()
    if resp_minus == "s":
         caracteres += minusculas
         break
    elif resp_minus == "n":
        break
    else: 
        print("Respuesta no valida. Por favor, elige una respuesta correcta s/n.")     
while True:
    resp_mayus = input("¿Deseas incluir letras mayusculas? (s/n): ").lower() 
    if resp_mayus == "s":
        caracteres += mayusculas
        break
    elif resp_mayus == "n":
        break
    else:
        print("Respuesta no valida. Por favor, elige una respuesta correcta s/n.")
while True:
    resp_numeros = input("¿Deseas incluir numeros? (s/n): ").lower()
    if resp_numeros == "s":
        caracteres += numeros
        break
    elif resp_numeros == "n":
        break
    else:
        print("Respuesta no valida. Por favor, elige una respuesta correcta s/n.")
while True:
    resp_simbolos = input("¿Deseas incluir simbolos? (s/n): ").lower()
    if resp_simbolos == "s":
        caracteres += simbolos
        break
    elif resp_simbolos == "n":
        break
    else:
        print("Respuesta no valida. Por favor, elige una respuesta correcta s/n.")
if caracteres == "":
    print("No se han seleccionado caracteres. Por favor, elige al menos un tipo de caracter.")

# 6 Crear una variable vacía para almacenar la contraseña generada
password = "" # aqui guardaremos la contraseña final

# 7 Repetir tantas veces como la longitud elegida por el usuario
for _ in range(length):
    # 8 Elegir un caracter aleatorio como la longitud elegida por el usuario
    char = secrets.choice(caracteres) # aqui se elige un caracter aleatorio de la variable caracteres
    # 9 Agregar el caracter elegido a la contraseña generada
    password += char # aqui se agrega el caracter a la contraseña final
# 10 Mostrar la contraseña generada al usuario
print("Tu contraseña generada es asi: ", password)






