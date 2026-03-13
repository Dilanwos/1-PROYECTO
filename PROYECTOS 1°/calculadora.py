print("=== CALCULADORA BASICA ===")

while True:
    numero1 = float(input("Ingresa el primer numero: "))
    numero2 = float(input("Ingresa el segundo numero: "))

    operacion = input("Elige la operacion (+, -, *, /): ")

    if operacion == "+":
        resultado = numero1 + numero2
        print("El resultado es:", resultado)

    elif operacion == "-":
        resultado = numero1 - numero2 
        print("El resultado es:", resultado)

    elif operacion == "*":
        resultado = numero1 * numero2
        print("El resultado es:", resultado)

    elif operacion == "/":
        if numero2 != 0:
            resultado = numero1 / numero2
            print("El resultado es:", resultado) 
        else: 
            print("Error: No se puede dividir por cero.")

    else: 
        print("Operacion no valida. Por favor, elija una operacion correcta.")
