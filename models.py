from extension import db  # Import the SQLAlchemy database instance from app.py 
from datetime import datetime, timezone


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Define an integer primary key column named 'id'
    name = db.Column(db.String(100), nullable=False)  # Define a string column named 'title' with a maximum length of 100 characters, cannot be null
    email = db.Column(db.String(120), nullable=False)  # Define a string column named 'email' with a maximum length of 120 characters, cannot be null
    subject = db.Column(db.String(200), nullable=False)  # Define a string column named 'subject' with a maximum length of 200 characters, cannot be null
    date = db.Column(db.DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))  # Define a DateTime column named 'date' with timezone support, defaulting to the current UTC time
    def __repr__(self):
        return f'{self.id} {self.name} {self.email} escribió {self.subject} el {self.date}'
    