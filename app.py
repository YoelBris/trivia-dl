
from flask import Flask, request, session, redirect, url_for
from Trivia import canciones, es_correcta

app = Flask(__name__)
app.secret_key = "trivia-dua-lipa"


ESTILOS = """
<style>
body {
    font-family: Arial, sans-serif;
    background: linear-gradient(135deg, #312e81, #0f172a);
    color: white;
    text-align: center;
    margin: 0;
    padding: 0;
}

.contenedor {
    max-width: 800px;
    margin: 80px auto;
    background: rgba(255,255,255,0.10);
    padding: 35px;
    border-radius: 20px;
    backdrop-filter: blur(10px);
}

h1 {
    font-size: 3em;
}

h2 {
    font-weight: normal;
}

.pista {
    font-size: 1.3em;
    margin: 25px 0;
    font-style: italic;
}

input {
    width: 70%;
    padding: 12px;
    border: none;
    border-radius: 10px;
    font-size: 16px;
}

button {
    padding: 12px 20px;
    border: none;
    border-radius: 10px;
    background-color: #22c55e;
    color: white;
    font-size: 16px;
    cursor: pointer;
}

button:hover {
    background-color: #16a34a;
}

.resultado {
    margin-top: 25px;
    font-size: 1.2em;
    font-weight: bold;
}

.correcto {
    color: #4ade80;
}

.incorrecto {
    color: #f87171;
}
</style>
"""


@app.route("/")
def bienvenida():

    session["pregunta"] = 0
    session["puntaje"] = 0

    return f"""
    <html>
    <head>
        <title>Trivia Dua Lipa</title>
        {ESTILOS}
    </head>

    <body>

        <div class="contenedor">

            <h1>🎵 Trivia Dua Lipa 🎵</h1>

            <h2>
                ¿Eres un verdadero fan de Dua Lipa? ⭐
            </h2>

            <p>
                Pon a prueba tus conocimientos
                intentando reconocer canciones
                a partir de fragmentos de sus letras.
            </p>

            <br>

            <form action="/trivia">
                <button type="submit">
                    Comenzar Trivia
                </button>
            </form>

        </div>

    </body>
    </html>
    """


@app.route("/trivia", methods=["GET"])
def trivia():

    indice = session.get("pregunta", 0)

    if indice >= len(canciones):
        return redirect(url_for("resultado_final"))

    cancion = canciones[indice]

    return f"""
    <html>
    <head>
        <title>Trivia Dua Lipa</title>
        {ESTILOS}
    </head>

    <body>

        <div class="contenedor">

            <h1>🎵 Trivia Dua Lipa 🎵</h1>

            <h2>
                Pregunta {indice + 1} de {len(canciones)}
            </h2>

            <div class="pista">
                "{cancion["pista"]}"
            </div>

            <form method="POST" action="/validar">

                <input
                    type="text"
                    name="respuesta"
                    placeholder="Escribe el nombre de la canción"
                    required>

                <br><br>

                <button type="submit">
                    Responder
                </button>

            </form>

        </div>

    </body>
    </html>
    """


@app.route("/validar", methods=["POST"])
def validar():

    indice = session.get("pregunta", 0)

    cancion = canciones[indice]

    respuesta_usuario = request.form.get("respuesta", "")

    correcta = es_correcta(
        respuesta_usuario,
        cancion["respuesta"]
    )

    if correcta:
        session["puntaje"] += 1

    session["ultima_correcta"] = correcta
    session["respuesta_correcta"] = cancion["respuesta"]

    return redirect(url_for("feedback"))


@app.route("/feedback")
def feedback():

    correcta = session.get("ultima_correcta", False)
    respuesta = session.get("respuesta_correcta", "")

    if correcta:
        mensaje = "✅ ¡Correcto!"
        clase = "correcto"
    else:
        mensaje = f"❌ Incorrecto. La respuesta era: {respuesta}"
        clase = "incorrecto"

    return f"""
    <html>
    <head>
        <title>Resultado</title>
        {ESTILOS}
    </head>

    <body>

        <div class="contenedor">

            <h1 class="{clase}">
                {mensaje}
            </h1>

            <br>

            <form action="/siguiente">

                <button type="submit">
                    Siguiente →
                </button>

            </form>

        </div>

    </body>
    </html>
    """


@app.route("/siguiente")
def siguiente():

    session["pregunta"] += 1

    return redirect(url_for("trivia"))


@app.route("/resultado")
def resultado_final():

    puntaje = session.get("puntaje", 0)

    if puntaje == len(canciones):
        mensaje = "🏆 ¡Perfecto! Eres un verdadero fan de Dua Lipa."
    elif puntaje >= len(canciones) // 2:
        mensaje = "👏 ¡Muy bien!"
    else:
        mensaje = "🎵 Sigue escuchando a Dua Lipa y vuelve a intentarlo."

    return f"""
    <html>
    <head>
        <title>Resultado Final</title>
        {ESTILOS}
    </head>

    <body>

        <div class="contenedor">

            <h1>Resultado Final</h1>

            <h2>
                Puntaje: {puntaje} / {len(canciones)}
            </h2>

            <p>
                {mensaje}
            </p>

            <br>

            <form action="/">

                <button type="submit">
                    🔄 Volver a Intentar
                </button>

            </form>

        </div>

    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(debug=True)
