from flask import Flask, render_template, request, redirect, url_for, flash
from extension import db  # Import the SQLAlchemy instance
from models import Task  # Import the Task model
from form import Formulario  # Import the Formulario class
from datetime import date

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'  # Configure the database URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable track modifications to save resources
app.config['SECRET_KEY'] = "miclaveultrasecreta123"

db.init_app(app)  # Initialize the SQLAlchemy instance with the Flask app

@app.route('/')
@app.route('/index', methods=['GET','POST'])
def send():
    formulario = Formulario()
    if formulario.validate_on_submit():
        try:
            print('listo texto', formulario.name.data)
            t = Task(name=formulario.name.data, email=formulario.email.data, subject=formulario.subject.data)
            db.session.add(t)
            db.session.commit()
            flash('Formulario enviado correctamente')
        except Exception as e:    
            db.session.rollback()
            print(f"Error al guardar tarea: {e}")
            flash('Ocurrió un error al enviar el formulario')
    
    task = Task.query.all()
    return render_template('index.html', formulario=formulario , task=task)

@app.route('/admin')
def admin_panel():
    codigo = request.args.get('codigo')  # obtiene ?codigo=loquesea

    if codigo != "isabella13":
        flash("Acceso denegado. Código inválido.")
        return redirect(url_for('send'))  # redirige al formulario

    try:
        tasks = Task.query.all()
    except Exception as e:
        print(f"Error al obtener tareas: {e}")
        tasks = [] # Fallback si hay un problema con la DB
    return render_template('admin.html', tasks=tasks)

@app.route('/delete/<int:id>', methods=['POST'])
def delete_task(id):
    try:
        task = Task.query.get_or_404(id)  # Obtiene la tarea por ID o devuelve 404 si no existe

        db.session.delete(task)  # Elimina la tarea de la sesión
        db.session.commit()  # Guarda los cambios en la base de datos
        flash('Tarea eliminada correctamente')

    except Exception as e:
        db.session.rollback()
        flash(f'Error al eliminar la tarea: {e}')
        print(f"Error al eliminar tarea: {e}")

    return redirect(url_for('admin_panel'))  # Redirige al panel de administración    

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)