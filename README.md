# Adivina-el-numero
Mi primer juego de código Python

Pseudocodigo (mejorado):

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


