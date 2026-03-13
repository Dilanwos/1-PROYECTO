# def cajero_automatico(saldo_actual, cantidad_a_retirar):
#     print(f"Saldo inicial: {saldo_actual}")
    
#     if cantidad_a_retirar <= saldo_actual:
#         # Bug: Restamos pero no guardamos el nuevo valor en 'saldo_actual'
#         saldo_actual -= cantidad_a_retirar
#         print(f"Retiro exitoso. Nuevo saldo: {saldo_actual}")
#     else:
#         print("No tienes suficientes monedas.")

# # Zona de pruebas
# mi_dinero = 100
# cajero_automatico(mi_dinero, 20)

def es_palindromo(palabra):
    # Invertimos la palabra usando slicing
    palabra_invertida = palabra[::-1]
    
    # Bug: Usamos un solo = (asignación) en lugar de == (comparación)
    # Por regla de Python, aquí dará error de sintaxis, o si usamos 'if palabra_invertida == palabra_invertida' siempre será True.
    # Usemos este bug lógico:
    if palabra == palabra_invertida: 
        print(f"¡Magia! La palabra '{palabra}' es un palíndromo.")
    else:
        print("No es un palíndromo.")

# Zona de pruebas
es_palindromo("ana")


