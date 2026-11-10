num1 = int(input("Introduce un numero: "))
num2 = int(input("Introduce otro numero: "))
operador = input("introduzca un operador (+,-,/,*): ")

if operador == "+":
    print(num1 + num2)
elif operador == "-":
    print(num1 - num2)
elif operador == "/" and num2 == 0:
    print("No puedes dividir entre cero")
elif operador == "/":
    print(num1 / num2)
elif operador == "*":
    print(num1 * num2)
else:
    print("Operación no valida")