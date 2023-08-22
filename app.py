from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

users_file = 'users.json'

def save_users(users_data):
    with open(users_file, 'w') as users_file:
        json.dump(users_data, users_file, indent=4)

def load_users():
    if os.path.exists(users_file):
        with open(users_file, 'r') as users_file:
            return json.load(users_file)
    else:
        return {"usuarios": []}

@app.route('/')
def hello_world():
    return '¡Hola, mundo! Esta es mi primera API con Flask.'

@app.route('/saludo/<nombre>', methods=['GET', 'POST'])
def saludar(nombre):
    if request.method == 'GET':
        return f'¡Hola, {nombre}! Bienvenido a mi API.'
    elif request.method == 'POST':
        return f'Hola, {nombre}! Tu saludo ha sido enviado por POST.'

@app.route('/json')
def json_response():
    data = {
        'mensaje': 'Esta es una respuesta JSON desde mi API.',
        'valor': 42
    }
    return jsonify(data)

@app.route('/signup', methods=['POST'])
def sign_up():
    new_user = request.get_json()
    users_data = load_users()
    users_data['usuarios'].append(new_user)
    save_users(users_data)
    return jsonify({"message": "Usuario registrado exitosamente"})

@app.route('/login', methods=['POST'])
def login():
    user_data = request.get_json()
    users_data = load_users()
    for user in users_data['usuarios']:
        if user['usuario'] == user_data['usuario'] and user['contraseña'] == user_data['contraseña']:
            return jsonify({"message": "Inicio de sesión exitoso"})
    return jsonify({"message": "Credenciales inválidas"})

@app.route('/users', methods=['GET', 'POST'])
def manage_users():
    if request.method == 'GET':
        users_data = load_users()
        return jsonify(users_data)
    elif request.method == 'POST':
        new_user = request.get_json()
        users_data = load_users()
        users_data['usuarios'].append(new_user)
        save_users(users_data)
        return jsonify({"message": "Usuario agregado exitosamente"})

@app.route('/users/<int:user_id>', methods=['GET', 'PUT', 'DELETE'])
def manage_user(user_id):
    users_data = load_users()
    if user_id >= 0 and user_id < len(users_data['usuarios']):
        if request.method == 'GET':
            return jsonify(users_data['usuarios'][user_id])
        elif request.method == 'PUT':
            updated_user = request.get_json()
            users_data['usuarios'][user_id] = updated_user
            save_users(users_data)
            return jsonify({"message": "Usuario actualizado exitosamente"})
        elif request.method == 'DELETE':
            users_data['usuarios'].pop(user_id)
            save_users(users_data)
            return jsonify({"message": "Usuario eliminado exitosamente"})
    else:
        return jsonify({"message": "Usuario no encontrado"})

if __name__ == '__main__':
    app.run()
