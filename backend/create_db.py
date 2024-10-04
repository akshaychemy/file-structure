# create_db.py
from src.config.config import create_app, db

app = create_app()

with app.app_context():
    db.create_all()  # This creates all tables defined in your models
    print("Tables created or already exist.")
