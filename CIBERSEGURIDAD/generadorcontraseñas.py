print("=== GENERADOR DE CONTRASEÑAS ===") 

import string
import secrets

minusculas = string.ascii_lowercase
mayusculas = string.ascii_uppercase
numeros = string.digits
simbolos = string.punctuation

strength = input("Elige la fuerza de la contraseña (baja, media, alta): ").lower() 
if strength == "baja":
        caracteres = minusculas
elif strength == "media":
        caracteres = minusculas + mayusculas + numeros
elif strength == "alta":
        caracteres = minusculas + mayusculas + numeros + simbolos
else:
        print("Fuerza no valida. Por favor, elige una fuerza correcta.")
    

length = int(input("Elige la longitud de la contraseña (8, 12, 16): "))
if length in [8, 12, 16]:
    pass
while length not in [8,12,16]:
    length = int(input("Elige 8, 12 o 16: "))
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
    exit()

# 6 Crear una variable vacía para almacenar la contraseña generada
password = "" # aqui guardaremos la contraseña final


for _ in range(length):

    char = secrets.choice(caracteres) 

    password += char # aqui se agrega el caracter a la contraseña final

print("Tu contraseña generada es: ", password)







