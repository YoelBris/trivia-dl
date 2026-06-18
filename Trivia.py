import os


def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')


def es_correcta(respuesta_usuario, respuesta_correcta):
    return respuesta_usuario.strip() == respuesta_correcta.strip()


# Trivia de canciones de Dua Lipa

canciones = [
    {
        "pista": "If you don't wanna see me dancing with somebody...",
        "respuesta": "Don't Start Now"
    },
    {
        "pista": "One kiss is all it takes, fallin' in love with me...",
        "respuesta": "One Kiss"
    },
    {
        "pista": "Did a full one-eighty, crazy...",
        "respuesta": "Don't Start Now"
    },
    {
        "pista": "I got new rules, I count 'em...",
        "respuesta": "New Rules"
    },
    {
        "pista": "Physical, let's get physical...",
        "respuesta": "Physical"
    },
    {
        "pista": "We're good, we're good...",
        "respuesta": "We're Good"
    },
    {
        "pista": "I should've stayed at home, 'cause now there ain't no letting you go...",
        "respuesta": "Break My Heart"
    },
    {
        "pista": "Maybe we should switch careers",
        "respuesta": "These Walls"
    },
    {
        "pista": "Are you somebody who can go there?",
        "respuesta": "Training Season"
    },
    {
        "pista": "I used to think that I was made out of stone",
        "respuesta": "Love Again"
    }
]


def jugar_trivia():
    puntaje = 0
    limpiar_pantalla()
    print("=== TRIVIA DE CANCIONES DE DUA LIPA ===")
    print("Adivina el nombre de la canción según la pista.\n")

    for i, cancion in enumerate(canciones, start=1):
        print(f"Pregunta {i}")
        print("Pista:", cancion["pista"])

        respuesta_usuario = input("¿Qué canción es?: ").strip().lower()
        respuesta_correcta = cancion["respuesta"].strip().lower()

        if es_correcta(respuesta_usuario, respuesta_correcta):
            print("🎉 ¡Correcto!")
            puntaje += 1
        else:
            print(f"❌ Incorrecto. La respuesta era: {cancion['respuesta']}")

        input("\nPresiona Enter para continuar...")
        limpiar_pantalla()

    print("=== RESULTADO FINAL ===")
    print(f"Puntaje obtenido: {puntaje}/{len(canciones)}")

    if puntaje == len(canciones):
        print("🏆 ¡Perfecto! Eres un verdadero fan de Dua Lipa.")
    elif puntaje >= len(canciones) // 2:
        print("👏 ¡Muy bien!")
    else:
        print("🎵 Sigue escuchando a Dua Lipa y vuelve a intentarlo.")


if __name__ == "__main__":
    jugar_trivia()
