from app import app
from extension import db  # Import the SQLAlchemy database instance from the app module
from models import Task
from datetime import date

with app.app_context():
	t = Task(title='Nuevo mensaje', date=date.today())  # Create a new Task instance with a title and today's date
	db.session.add(t)  # Add the new task to the current database session
	db.session.commit()  # Commit the session to save the new task to the database

print("✅ Tarea agregada correctamente")  # Print a success message to the console
# This code creates a new task in the database using SQLAlchemy.


