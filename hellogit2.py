print ("Juego de la raza malvada contra la benevola")
print ("Ingresa la raza malvada")
malvada = ["lolos","fulanos","hoggins","lurcos","trollis"]
cantMalos = {}
for malos in malvada:
    cantMalos[malos] = input(f"Introduce una cantidad de soldados {malos}: ")

print ("Ingresa la raza benevola")
benevola = ["ositos","principes","enanos","caris","fulos"]
cantBuenos = {}
for buenos in benevola:
    cantBuenos[buenos] = input(f"Introduce una cantidad de soldados {buenos}: ")

totalMalvada = 0
suma = 1
for poderM in cantMalos:
    totalMalvada += int(cantMalos[poderM]) * suma
    suma += 1

totalBuenos = 0
suma = 1
for poderB in cantBuenos:
    totalBuenos += int(cantBuenos[poderB]) * suma
    suma += 1

print (f"El total de poder de soldados malos es de: {totalMalvada}")
print (f"El total de poder de soldados buenos es de: {totalBuenos}")

print ("El resultado es:")
if totalMalvada > totalBuenos:
    print("El resultado es: gana el mal")
elif totalBuenos > totalMalvada:
    print("El resultado es: gana el bien")
else:
    print("El resultado es: empate")