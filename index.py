from flask import Flask, render_template

app = Flask(__name__)

num1 = 5
num2 = 10
sum = num1 + num2
nombre = "Luis"

# @app.route('/')
# def home():
#     return f"<h1>Mi primer pagina web con python </h1> {sum} {nombre}"

# @app.route('/contacto')
# def contacto():
#     return f"<h1> Hola {nombre}, esta es la pagina de contacto </h1>"

@app.route('/')
def principal():
    return render_template('principal.html')

@app.route('/lenguajes')
def mostrarLenguajes():
    misLenguajes=("Python", "Java", "Go", "JavaScript", "Ruby", "Perl")
    return render_template('lenguajes.html', lenguajes=misLenguajes)

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

if __name__ == '__main__':
    app.run(debug=True, port=5017)  