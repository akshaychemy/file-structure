# /Users/krishnamayekar/Desktop/login/backend/app.py
from src.config.config import create_app, db  # Import 'db' from config.py
from src.routes.user_bp import user_bp  # Import blueprint from the routes folder

app = create_app()

# Register Blueprints
app.register_blueprint(user_bp, url_prefix="/users")

# Main entry point of the application
if __name__ == "__main__":
    # Create all database tables (if they do not exist) within the app context
    with app.app_context():
        db.create_all()  # Create all tables defined in your models
    # Run the Flask development server with debug mode enabled
    app.run(debug=True)
