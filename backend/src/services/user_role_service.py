from src.models.all_models import User, db
from flask_jwt_extended import create_access_token
from src.config.config import bcrypt
import uuid

def signup(data, user_info):
    try:
        if "username" in data and "email" in data and "password" in data:
            username = data["username"]
            email = data["email"]
            password = data["password"]

            # Hash the password using bcrypt
            hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

            # Create a new user object
            new_user = User(
                id=str(uuid.uuid4()),  # Assuming UUID as a string
                username=username,
                email=email,
                password=hashed_password  # Store the hashed password
            )

            db.session.add(new_user)
            db.session.commit()
            return {'status': "success", "statusCode": 201, "message": "User created successfully!"}, 201
        else:
            return {'status': "failed", "statusCode": 400, "message": "Username, email, and password are required"}, 400
    except Exception as e:
        db.session.rollback()
        return {'status': "failed", "statusCode": 500, "message": "Error occurred", "error": str(e)}, 500

def login(data):
    try:
        if "email" in data and "password" in data:
            user = User.query.filter_by(email=data["email"]).first()
            if user and bcrypt.check_password_hash(user.password, data["password"]):
                access_token = create_access_token(identity=user.id)
                return {'status': "success", "statusCode": 200, "access_token": access_token}, 200
            else:
                return {'status': "failed", "statusCode": 401, "message": "Invalid credentials!"}, 401
        else:
            return {'status': "failed", "statusCode": 400, "message": "Email and password are required"}, 400
    except Exception as e:
        return {'status': "failed", "statusCode": 500, "message": "Error occurred", "error": str(e)}, 500

def get_profile(user_id):
    try:
        user = User.query.get(user_id)
        if user:
            user_data = {
                "username": user.username,
                "email": user.email
            }
            return {'status': "success", "statusCode": 200, "message": "User profile found", "data": user_data}, 200
        else:
            return {'status': "failed", "statusCode": 404, "message": "User not found"}, 404
    except Exception as e:
        return {'status': "failed", "statusCode": 500, "message": "Error occurred", "error": str(e)}, 500

# @log_function_execution
def logout(user_info):
    try:
        # Normally, the frontend will handle removing the JWT token.
        return {'status': "success", "statusCode": 200, "message": "Logged out successfully!"}, 200
    except Exception as e:
        return {'status': "failed", "statusCode": 500, "message": "Error occurred", "error": str(e)}, 500
