from flask import Flask, render_template, request

app=Flask(__name__)

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
        return resultado  # Devuelve el resultado directo como HTML

    return render_template("cinepolis.html")
    

if __name__ == "__main__":
    app.run(debug=True, port=3000)
