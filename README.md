# Adivina-el-numero
Mi primer juego de código Python

Pseudocodigo:

INICIO DEL PROGRAMA

best_score = None
seguir_jugando = "s"

MIENTRAS seguir_jugando == "s":

    Generar numero_secreto entre 1 y 100
    intentos = 0

    Mostrar mensaje de bienvenida

    MIENTRAS True:
        Pedir número al usuario

        SI no es un número válido:
            Mostrar error
            Continuar

        Convertir a entero
        intentos += 1

        SI intento < numero_secreto:
            Mostrar "Más alto"
        SINO SI intento > numero_secreto:
            Mostrar "Más bajo"
        SINO:
            Mostrar "¡Has acertado!"
            Mostrar número de intentos
            Actualizar best_score si corresponde
            SALIR del bucle

    Preguntar si quiere jugar otra vez (s/n)
    Guardar respuesta en seguir_jugando

Mostrar mensaje final de despedida

FIN DEL PROGRAMA


Codigo del juego:

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
