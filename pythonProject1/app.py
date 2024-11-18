from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('Pagina principal.html')


@app.route("/Boton ejercicio 1", methods=['GET', 'POST'])
def formulario():
    resultado = None
    if request.method == "POST":
        try:
            Nota1 = float(request.form.get('Nota1', 0))
            Nota2 = float(request.form.get('Nota2', 0))
            Nota3 = float(request.form.get('Nota3', 0))
            Asistencia = float(request.form.get('Asistencia', 0))

            # Validar rangos
            if not (10 <= Nota1 <= 70 and 10 <= Nota2 <= 70 and 10 <= Nota3 <= 70 and 0 <= Asistencia <= 100):
                resultado = "Error: Las notas deben estar entre 10 y 70, y la asistencia entre 0 y 100."
            elif not (0 <= Asistencia <= 100):
                resultado = "La asistencia debe estar entre 0% y 100%."
            else:
                promedio = (Nota1 + Nota2 + Nota3) / 3  # Calcular promedio

                if promedio >= 40 and Asistencia >= 75:  # Determinar estado
                    resultado = f"Promedio: {promedio:.2f}. Estado: Aprobado."
                else:
                    resultado = f"Promedio: {promedio:.2f}. Estado: Reprobado."
        except ValueError:
            resultado = "Error: Por favor, ingrese valores válidos."

    return render_template("Boton ejercicio 1.html", resultado=resultado)


@app.route("/Boton ejercicio 2", methods=["GET", "POST"])
def ejercicio2():
    resultado = None
    if request.method == "POST":
        try:
            nombre1 = request.form.get("nombre1", "").strip()
            nombre2 = request.form.get("nombre2", "").strip()
            nombre3 = request.form.get("nombre3", "").strip()

            if not nombre1 or not nombre2 or not nombre3:
                resultado = "Error: Todos los nombres deben estar completos."
            elif len(set([nombre1, nombre2, nombre3])) < 3:
                resultado = "Error: Los nombres deben ser diferentes."
            else:
                nombres = [nombre1, nombre2, nombre3]
                nombre_mas_largo = max(nombres, key=len)
                longitud = len(nombre_mas_largo)

                resultado = f"El nombre más largo es '{nombre_mas_largo}' con {longitud} caracteres."
        except Exception as e:
            resultado = f"Error inesperado: {e}"

    return render_template("Boton ejercicio 2.html", resultado=resultado)


if __name__ == '__main__':
    app.run(debug=True)
