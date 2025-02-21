from flask import Flask, render_template, request
import forms
import formsZodiaco
from datetime import datetime
from flask import g
from flask import flash
from flask_wtf.csrf import CSRFProtect


app=Flask(__name__)
app.secret_key='esta es una clave secreta'
csrf=CSRFProtect()


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.after_request
def after_request(response):
    print('after 1')
    return response

@app.before_request
def before_request():
    g.nombre='Mario'
    print('before 1')

@app.route("/")
def index():
    titulo="IDGS805"
    lista=["Pedro", "Juan", "Mario"]
    return render_template("index.html",titulo=titulo,lista=lista)


@app.route("/ejemplo1")
def ejemplo1():
    return render_template("ejemplo1.html")

@app.route("/ejemplo2")
def ejemplo2():
    return render_template("ejemplo2.html")

@app.route("/Hola")
def hola():
    return "Hola Mundo!!"

@app.route("/user/<string:user>")
def user(user):
    return f"Hola, {user}!"

@app.route("/numero/<int:n>")
def numero(n):
    return f"El numero es: {n}"

@app.route("/user/<int:id>/<string:username>")
def username(id,username):
    return f"El usuario es: {username} con id: {id}"

@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1,n2):
    return f"La suma es: {n1+n2}"

@app.route("/default/")
@app.route("/default/<string:tem>")
def func1(tem='Juan'):
    return f"Hola, {tem}!"

@app.route("/form1/")
def form1():
    return '''
            <form>
            <label for="nombre">Nombre:</lable>
            <input type="text" id="nombre" name="nombre"> </input>
            </form>

            '''
            

@app.route("/OperasBas")
def operas():
    return render_template("OperasBas.html")

@app.route("/resultado", methods=["GET", "POST"])
def result():
    if request.method == "POST":
        num1 = request.form.get("n1")
        num2 = request.form.get("n2")
        return "La multiplicacion de {} x {} = {}".format(num1,num2,str(int(num1)*int(num2))) 
    

class CinepolisVenta:
    def __init__(self):
        self.total_dia = 0

    def calcular_descuento(self, subtotal, total_boletos, tarjeta_cineco):
        """Calcula el descuento según la cantidad de boletos y si tiene tarjeta Cineco"""
        descuento = subtotal * (0.15 if total_boletos > 5 else 0.10 if total_boletos >= 3 else 0)
        if tarjeta_cineco:
            descuento += (subtotal - descuento) * 0.10
        return descuento

    def procesar_venta(self, nombre, num_personas, total_boletos, tarjeta_cineco):
        """Procesa la venta y devuelve el resultado como texto"""
        if total_boletos > num_personas * 7:
            return f"Error: El número de boletos ({total_boletos}) excede el límite de 7 por persona.\n Por favor cambia el numero de personas o boletos"

        subtotal = total_boletos * 12
        descuento = self.calcular_descuento(subtotal, total_boletos, tarjeta_cineco)
        total_a_pagar = subtotal - descuento
        self.total_dia += total_a_pagar

        return f"""
        <h2>Resumen de la compra</h2>
        <p><strong>Comprador:</strong> {nombre}</p>
        <p><strong>Personas:</strong> {num_personas}</p>
        <p><strong>Boletos:</strong> {total_boletos}</p>
        <p><strong>Subtotal:</strong> ${subtotal:.2f}</p>
        <p><strong>Descuento:</strong> ${descuento:.2f}</p>
        <p><strong>Total a Pagar:</strong> ${total_a_pagar:.2f}</p>
        """

cinepolis = CinepolisVenta()

@app.route("/Cinepolis", methods=["GET", "POST"])
def Cinepolis():
    if request.method == "POST":
        nombre = request.form.get("nombre")
        num_personas = int(request.form.get("num_personas", 0))
        total_boletos = int(request.form.get("total_boletos", 0))
        tarjeta_cineco = request.form.get("tarjeta_cineco") == "si"

        resultado = cinepolis.procesar_venta(nombre, num_personas, total_boletos, tarjeta_cineco)
        return resultado 

    return render_template("cinepolis.html")
    

@app.route("/alumnos", methods = ["GET", "POST"])
def alumnos():
    print('alumno:{}'.format(g.nombre))
    mat = ''
    nom = ''
    ape = ''
    email = ''
    alumno_clase = forms.UserForm(request.form)
    if request.method == "POST" and alumno_clase.validate():
        mat = alumno_clase.matricula.data
        ape = alumno_clase.apellido.data
        nom = alumno_clase.nombre.data
        email = alumno_clase.email.data
        memsaje='Bienvenido {}', format(nom)
        flash(message)
    
    return render_template("Alumnos.html", form = alumno_clase, mat = mat, ape = ape, nom = nom, email = email)


def calcular_signo_chino(anio):
    signos = ["Rata", "Buey", "Tigre", "Conejo", "Dragón", "Serpiente", "Caballo", "Cabra", "Mono", "Gallo", "Perro", "Cerdo"]
    return signos[(anio - 1900) % 12]  # 1900 es el año de la Rata

def obtener_imagen_chino(signo):
    nombres_imagenes = {
        "Rata": "Rata.png",
        "Buey": "Buey.png",
        "Tigre": "Tigre.png",
        "Conejo": "Conejo.png",
        "Dragón": "Dragon.png",
        "Serpiente": "Serpiente.png",
        "Caballo": "Caballo.png",
        "Cabra": "Cabra.png",
        "Mono": "Mono.png",
        "Gallo": "Gallo.png",
        "Perro": "Perro.png",
        "Cerdo": "Cerdo.png"
    }
    return nombres_imagenes.get(signo, "default.png")

def calcular_edad(dia, mes, anio):
    hoy = datetime.today()
    edad = hoy.year - anio - ((hoy.month, hoy.day) < (mes, dia))
    return edad

@app.route("/zodiaco", methods=["GET", "POST"])
def zodiaco():
    nom = ''
    apep = ''
    apem = ''
    dia = ''
    mes = ''
    anio = ''
    sexo = ''
    signo = ''
    imagen = ''
    edad = ''
    
    generar_zodiaco = formsZodiaco.FormZodiaco(request.form)
    
    if request.method == "POST" and generar_zodiaco.validate():
        nom = generar_zodiaco.nombre.data
        apep = generar_zodiaco.apellido_paterno.data
        apem = generar_zodiaco.apellido_materno.data
        dia = generar_zodiaco.dia.data
        mes = generar_zodiaco.mes.data
        anio = generar_zodiaco.anio.data
        sexo = generar_zodiaco.sexo.data
        
        signo = calcular_signo_chino(anio) 
        imagen = obtener_imagen_chino(signo) 
        edad = calcular_edad(dia, mes, anio)
    
    return render_template("zodiaco.html", 
                           nom=nom, apep=apep, apem=apem, 
                           dia=dia, mes=mes, anio=anio, 
                           sexo=sexo, signo=signo, 
                           imagen=imagen, edad=edad,
                           form=generar_zodiaco)


if __name__ == "__main__":
    csrf.init_app(app)
    app.run(debug=True, port=3000)
