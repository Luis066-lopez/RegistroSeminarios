from flask import Flask, render_template, request, redirect, url_for
import cx_Oracle

app = Flask(__name__)

# Página de Inicio
@app.route('/')
def home():
    return render_template('index.html')

# Página Quiénes Somos
@app.route('/about')
def about():
    return render_template('about.html')

# Página Servicios
@app.route('/services')
def services():
    return render_template('services.html')

# Página de Noticias
@app.route('/news')
def news():
    return render_template('news.html')

# Página de Contacto
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        # lógica para manejar el envío del mensaje
        return redirect(url_for('contact'))
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
