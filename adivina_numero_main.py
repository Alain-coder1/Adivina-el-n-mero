import random

def pedir_numero():
    """Pide un número válido entre 1 y 100 y lo devuelve como entero."""
    while True:
        entrada = input("Introduce un número entre 1 y 100: ")

        try:
            numero = int(entrada)
        except ValueError:
            print("Por ahí no. Debes introducir un número válido.")
            continue

        if numero < 1 or numero > 100:
            print("¡No hagas trampa! El número debe estar entre 1 y 100.")
            continue

        return numero


def jugar_partida():
    """Ejecuta una partida completa y devuelve el número de intentos."""
    numero_secreto = random.randint(1, 100)
    intentos = 0

    print("\nBienvenido al juego Adivina el número")
    print("He pensado un número entre 1 y 100. ¡Intenta adivinarlo!")

    while True:
        intento = pedir_numero()
        intentos += 1

        if intento < numero_secreto:
            print("Más alto")
        elif intento > numero_secreto:
            print("Más bajo")
        else:
            print(f"¡Máquina, has acertado! El número era {numero_secreto}.")
            print(f"Has necesitado {intentos} intentos.")
            return intentos


def main():
    """Controla el flujo general del juego y el récord."""
    best_score = None
    seguir_jugando = "s"

    while seguir_jugando == "s":
        intentos = jugar_partida()

        if best_score is None or intentos < best_score:
            best_score = intentos
            print("¡Nuevo récord personal!")

        seguir_jugando = input("¿Quieres echar otra partida? (s/n): ").lower().strip()

    print("\nGracias por jugar. Tu mejor puntuación fue:", best_score)
    print("¡Vuelve pronto!")



if __name__ == "__main__":
    main()