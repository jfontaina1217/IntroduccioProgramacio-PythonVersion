print("============== Calculadora de IPs de Joaquin en Python ================")
octeto1 = int(input("Introduzca el primer octeto: "))
octeto2 = int(input("Introduzca el segundo octeto: "))
octeto3 = int(input("Introduzca el tercero octeto: "))
octeto4 = int(input("Introduzca el cuarto octeto: "))

if octeto1 >= 0 and octeto1 <= 255 and octeto2 >= 0 and octeto2 <= 255 and octeto3 >= 0 and octeto3 <= 255 and octeto4 >= 0 and octeto4 <= 255:
    print()
    print(f"La IP introducida es: {octeto1}.{octeto2}.{octeto3}.{octeto4}")
    correcta = True
else:
    print("La IP introducida es incorrecta.")
    correcta = False

mascdefecte = "No hi ha per defecte"
if octeto1 >= 1 and octeto1 <= 12:
    clase = "A"
    mascdefecte = "255.0.0.0"
elif octeto1 == 127:
    clase = "Loopback"
elif octeto1 >= 128 and octeto1 <= 191:
    clase = "B"
    mascdefecte = "255.255.0.0"
elif octeto1 >= 192 and octeto1 <= 223:
    clase = "C"
    mascdefecte = "255.255.255.0"
elif octeto1 >= 224 and octeto1 <= 239:
    clase = "D"
elif octeto1 >= 240 and octeto1 <= 255:
    clase = "E"
elif octeto1 == 0:
    clase = "Reservada"
else:
    clase = "Invalida"

if octeto1 == 10:
    privada = True
elif octeto1 == 172 and octeto2 >= 16 and octeto2 <= 31:
    privada = True
elif octeto1 == 192 and octeto2 == 168:
    privada = True
else:
    privada = False

if correcta == True:
    print(f"Clase: {clase}")
    print(f"Mascara por defecto: {mascdefecte}")
if privada == True:
    print("Tipus: Privada")
elif clase != "Loopback":
    print("Tipus: Publica")