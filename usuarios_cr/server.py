from flask import Flask,render_template,redirect,request
app=Flask(__name__)

from usuarios import Usuario


@app.route('/')
def index():
    return redirect('/users')

@app.route("/users")
def todos_los_usuarios():
    # llamar al método de clase get all para obtener todos los usuarios
    usuarios = Usuario.get_all()
    print(usuarios)
    return render_template("todos_los_usuarios.html", todos_los_usuarios=usuarios)


@app.route('/process', methods=["POST"])
def procesar_usuario():
    # Primero hacemos un diccionario de datos a partir de nuestro request.form proveniente de nuestra plantilla
    # Las claves en los datos tienen que alinearse exactamente con las variables en nuestra cadena de consulta
    data = {
        "first_name": request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"]
    }
    # Pasamos el diccionario de datos al método save de la clase Usuario
    Usuario.save(data)
    # No olvides redirigir después de guardar en la base de datos
    return redirect('/users')


@app.route('/users/new')
def nuevo_usuario():
    return render_template('nuevo_usuario.html')



if __name__=="__main__":
    app.run(debug=True)