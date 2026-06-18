from flask import Flask, request
from Trivia import es_correcta

app = Flask(__name__)

PISTA = "Maybe we should switch careers"
RESPUESTA = "These Walls"

@app.route("/", methods=["GET", "POST"])
def inicio():

    resultado = ""

    if request.method == "POST":
        respuesta_usuario = request.form.get("respuesta", "")

        if es_correcta(respuesta_usuario, RESPUESTA):
            resultado = "✅ ¡Correcto!"
        else:
            resultado = f"❌ Incorrecto. La respuesta era: {RESPUESTA}"

    return f"""
    <h1>🎵 Trivia Dua Lipa</h1>

    <p><b>Pista:</b> {PISTA}</p>

    <form method="POST">
        <input type="text" name="respuesta">
        <button type="submit">Responder</button>
    </form>

    <p>{resultado}</p>
    """

if __name__ == "__main__":
    app.run(debug=True)