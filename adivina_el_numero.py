import random

best_score = None 
seguir_jugando = "s"

while seguir_jugando == "s":

    numero_secreto = random.randint(1, 100)
    intentos = 0

    print("\nBienvenido al juego Adivina el número ")
    print("He pensado un número entre 1 y 100. ¡Intenta adivinarlo!")

    while True:
        entrada = input("Introduce un número entre 1 y 100: ")

        # Validación
        try:
            intento = int(entrada)
        except:
            print("Por ahí no. Debes introducir un número válido.")
            continue

        if intento < 1 or intento > 100:
            print("¡No hagas trampa! El número debe estar entre 1 y 100.")
            continue

        intentos += 1

        # Comparación
        if intento < numero_secreto:
            print("Más alto")
        elif intento > numero_secreto:
            print("Más bajo")
        else:
            print(f"¡Máquina, has acertado! El número era {numero_secreto}.")
            print(f"Has necesitado {intentos} intentos.")

            # Actualizar récord
            if best_score is None or intentos < best_score:
                best_score = intentos
                print("Nuevo récord personal!")

            break

    seguir_jugando = input("¿Quieres echar otra partida? (s/n): ").lower()
print("\nGracias por jugar. Tu mejor puntuación fue:", best_score) 
print("¡Vuelve pronto!")