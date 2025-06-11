import random


print("juego de adivinar el numero")

maxNum = int(input("introduzca el numero tope para el rango: "))

while maxNum <= 0:
    try:
        maxNum = int(input("introduzca un numero para el rango: "))
        if maxNum <= 0:
            print("introduzca un numero mayor que 0")
    except ValueError:
        print("introduzca un numero entero valido")

numAdivinado = random.randint(1, maxNum)
intenMax = 20
intentosmaximos= max(1, maxNum // 20)
resultados = ["fallaste :( "] * maxNum
resultados[numAdivinado - 1] = "le atino :)"
intentos = 0
acertado = False

while intentos < intenMax and  acertado != True:
    try:
        adivina = int(input(f"intento {intentos + 1}: introduzca su numero: "))
        intentos += 1
        if adivina == numAdivinado:
            print("felicitaciones adivino el numero")
            acertado = True
        elif adivina < numAdivinado:
            print("el numero a adivinar es mayor")
        else:
            print("el numero a adivinar es menor")
    except ValueError:
        print("no es un numero entero valido")
        intentos += 1

if acertado != True:
    print(f"has intentado y no lograste tus {intenMax} intentos, El numero era {numAdivinado}")

print(f"Resultados: {resultados}")
print(f"Intentos realizados: {intentos}")



print(f"Has seleccionado un rango de 1 a {maxNum} y tenias {intenMax} intentos para adivinar el numero")