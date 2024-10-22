from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def menu():
    return render_template('menu.html')

@app.route('/inscripcion', methods=['GET', 'POST'])
def inscripcion():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellidos = request.form['apellidos']
        curso = request.form['curso']
        return f"Inscripción recibida: {nombre} {apellidos}, curso: {curso}"
    return render_template('inscripcion.html')

@app.route('/registro_usuarios', methods=['GET', 'POST'])
def registro_usuarios():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellidos = request.form['apellidos']
        email = request.form['email']
        contrasena = request.form['contrasena']
        return f"Usuario registrado: {nombre} {apellidos}, email: {email}"
    return render_template('registro_usuarios.html')

@app.route('/registro_productos', methods=['GET', 'POST'])
def registro_productos():
    if request.method == 'POST':
        producto = request.form['producto']
        categoria = request.form['categoria']
        existencia = request.form['existencia']
        precio = request.form['precio']
        return f"Producto registrado: {producto}, categoría: {categoria}, existencia: {existencia}, precio: {precio}"
    return render_template('registro_productos.html')

@app.route('/registro_libros', methods=['GET', 'POST'])
def registro_libros():
    if request.method == 'POST':
        titulo = request.form['titulo']
        autor = request.form['autor']
        resumen = request.form['resumen']
        modo = request.form['modo']
        return f"Libro registrado: {titulo} por {autor}, modo: {modo}"
    return render_template('registro_libros.html')

if __name__ == '__main__':
    app.run(debug=True)
