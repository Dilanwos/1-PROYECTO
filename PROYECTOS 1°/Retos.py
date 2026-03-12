# num1 = float(input("Ingresa el primer numero: "))
# num2 = float(input("Ingresa el segundo numero: "))

# operacion = input("Elige la operacion (+, -, *, /): ")

# def calculadora(num1, num2, operacion):
#     resultado = 0
#     if operacion == "+":
#         resultado = num1 + num2
#     elif operacion == "-":
#         resultado = num1 - num2  # ¡Cuidado aquí!
#     elif operacion == "*":
#         resultado = num1 * num2
#     elif operacion == "/":
#         resultado = num1 / num2
#     print(f"El resultado es: {resultado}")

# # Zona de pruebas
# calculadora(num1, num2, operacion) 

# def contar_vocales(palabra):
#     contador = 0
#     vocales = "aeiou"
    
#     for letra in palabra:
#         if letra in vocales:
#             contador = contador + 1
            
#     return contador # El retorno está en el lugar equivocado

# # Zona de pruebas
# contador = contar_vocales("murcielago")
# print(f"Total de vocales: {contador}")

# def agregar_al_inventario(inventario, nuevo_objeto):
#     # inventario = ["Espada", "Escudo", "Mapa"]
#     inventario.append(nuevo_objeto)
        
    
#     # Bug: Sobrescribimos la lista con una cadena de texto
#     print(f"Has agregado {nuevo_objeto} a tu inventario.")
#     print(f"Tienes {len(inventario)} objetos en tu mochila.")

# # Zona de pruebas
# inventario = ["Espada", "Escudo", "Mapa"]
# agregar_al_inventario(inventario, "Poción de vida")
# agregar_al_inventario(inventario, "Poción de mana")