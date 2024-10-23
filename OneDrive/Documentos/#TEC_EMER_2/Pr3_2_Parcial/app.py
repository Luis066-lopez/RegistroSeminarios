from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'clave_secreta'

# Lista global de registros
registros = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Obtener datos de los formularios
        fecha = request.form['fecha']
        nombre = request.form['nombre']
        apellidos = request.form['apellidos']
        turno = request.form['turno']
        seminarios = request.form.getlist('seminarios')  # Obtener lista de seminarios seleccionados

        # Verifica que los datos lleguen correctamente
        print("Datos recibidos:", fecha, nombre, apellidos, turno, seminarios)

        # Crear un nuevo registro
        nuevo_registro = {
            'id': len(registros) + 1,
            'fecha': fecha,
            'nombre': nombre,
            'apellidos': apellidos,
            'turno': turno,
            'seminarios': seminarios
        }

        # Agregar registro a la lista global
        registros.append(nuevo_registro)

        # Redirigir a la página de lista de registros
        return redirect(url_for('lista_registros'))

    return render_template('index.html')


@app.route('/lista_registros')
def lista_registros():
    # Mostrar la lista de registros en la página de 'Lista de Registros'
    return render_template('lista_registros.html', registros=registros)


@app.route('/eliminar/<int:id>')
def eliminar(id):
    global registros
    # Filtrar los registros para eliminar el registro con el ID correspondiente
    registros = [r for r in registros if r['id'] != id]
    return redirect(url_for('lista_registros'))


@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    registro = next((r for r in registros if r['id'] == id), None)
    if not registro:
        return redirect(url_for('lista_registros'))
    
    if request.method == 'POST':
        # Actualizar los datos del registro
        registro['fecha'] = request.form['fecha']
        registro['nombre'] = request.form['nombre']
        registro['apellidos'] = request.form['apellidos']
        registro['turno'] = request.form['turno']
        registro['seminarios'] = request.form.getlist('seminarios')

        # Redirigir de nuevo a la lista de registros
        return redirect(url_for('lista_registros'))

    # Mostrar los datos en el formulario de edición
    return render_template('editar.html', registro=registro)


if __name__ == '__main__':
    app.run(debug=True)
