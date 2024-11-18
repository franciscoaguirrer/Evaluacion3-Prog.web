from flask import Flask, render_template, request

app = Flask(__name__)
app.debug = True

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ejercicio1", methods=["GET", "POST"])
def ejercicio1():
    if request.method == "POST":
        notas = [int(request.form[f"nota{i}"]) for i in range(1, 4)]
        asistencia = int(request.form["asistencia"])
        promedio = sum(notas) / 3
        estado = "Aprobado" if promedio >= 40 and asistencia >= 75 else "Reprobado"
        return render_template("ejercicio1.html", promedio=promedio, estado=estado)
    return render_template("ejercicio1.html")

@app.route("/ejercicio2", methods=["GET", "POST"])
def ejercicio2():
    if request.method == "POST":
        nombres = [request.form[f"nombre{i}"] for i in range(1, 4)]
        nombre_mas_largo = max(nombres, key=len)
        return render_template("ejercicio2.html", nombre=nombre_mas_largo, longitud=len(nombre_mas_largo))
    return render_template("ejercicio2.html")

if __name__ == "__main__":
    app.run()
