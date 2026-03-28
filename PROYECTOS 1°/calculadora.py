print("=== CALCULADORA BASICA ===")

while True:
    numero1 = float(input("Ingresa el primer numero: "))
    numero2 = float(input("Ingresa el segundo numero: "))

    operacion = input("Elige la operacion (+, -, *, /): ")

    if operacion == "+":
        resultado = numero1 + numero2

    elif operacion == "-":
        resultado = numero1 - numero2 

    elif operacion == "*":
        resultado = numero1 * numero2

    elif operacion == "/":
        if numero2 == 0:
            print("No se puede dividir entre 0")
            continue
        resultado = numero1 / numero2

    else: 
        print("Operacion no valida. Por favor, elija una operacion correcta.")
        continue

# Esto solo se ejecuta si la operacion es valida

    print("El resultado es:", resultado)
    break 