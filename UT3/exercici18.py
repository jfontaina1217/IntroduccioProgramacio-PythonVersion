edad = int(input("Por favor introduzca su edad "))
carnet = input("Dispone de carnet estudiantil? (Responda con Si o No). ")
preu = 20

if edad < 18 or edad > 65 or carnet == "Si":
    preu = preu - 5
print(f"El precio a pagar es de {preu}")
