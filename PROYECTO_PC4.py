import random

# La computadora elige un número del 1 al 100
numero_secreto = random.randint(1, 100)
intentos = 0

print("¡Bienvenido al juego de adivinanza!")
print("He pensado un número del 1 al 100. ¿Puedes adivinar cuál es?")

while intentos < 10:
    # El usuario introduce un número
    entrada = input("Escribe tu número: ")
    
    # Comprobamos que sea un número válido
    if not entrada.isdigit():
        print("Por favor, escribe un número válido.")
        continue
        
    intento = int(entrada)
    intentos += 1
    
    # Comparamos el número ingresado con el secreto
    if intento < numero_secreto:
        print("El número secreto es más alto.")
    elif intento > numero_secreto:
        print("El número secreto es más bajo.")
    else:
        print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
        break
else:
    print(f"Lo siento, has agotado tus intentos. El número secreto era {numero_secreto}.")