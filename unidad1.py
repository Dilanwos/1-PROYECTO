# # edad = int(input("Edad: "))
# nombre = input("¿Cual es tu nombre?" )
# print("Tu nombre letra por letra es")

# for letra in (nombre):
#     print(f"letra {letra}")

lista = ["Yamaha", "Honda", "Suzuki", "Kawasaki", "Ducati"]
for marca in lista:
    print(f"Marca: {marca}")

print("la que mas me gusta es:", lista[3])
print("La ultima marca de moto es:", lista[4])

lista.extend(["BMW", "Harley-Davidson"])

print("Lista actualizada:", lista)

lista = ["Yamaha", "Honda", "Suzuki", "Kawasaki", "Ducati"]
i = 0
while i < 1:
    print(f"La Marca {lista[i]} es mi favorita")
    i += 1