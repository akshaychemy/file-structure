from flask import request, Response, json, jsonify, g
from src.services import user_role_service
# from src.middlewares import authenticate_middleware, authenticate_admin

# @authenticate_admin
def signup():
    user_info = g.get('user_info')  # Extract user info if needed from middleware
    data = request.json
    response, status = user_role_service.signup(data, user_info)
    return Response(response=json.dumps(response), status=status, mimetype='application/json')

def login():
    data = request.json
    response, status = user_role_service.login(data)
    return Response(response=json.dumps(response), status=status, mimetype='application/json')

# @authenticate_middleware
def profile():
    # user_info = g.get('user_info')  # Authenticated user info
    response, status = user_role_service.get_profile(user_id)
    return Response(response=json.dumps(response), status=status, mimetype='application/json')

# @authenticate_middleware
def logout():
    user_info = g.get('user_info')  # Authenticated user info
    response, status = user_role_service.logout(user_info)
    return Response(response=json.dumps(response), status=status, mimetype='application/json')
