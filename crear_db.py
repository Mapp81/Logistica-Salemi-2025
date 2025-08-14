from app import app, db
from models import *

with app.app_context():
    db.create_all()
    print("✅ Base de datos creada correctamente")

# This code initializes the database for a Flask application using SQLAlchemy.
# It imports the app and db instances from the app module, and the models from the models module.