**Lab 01: Construcción de API con Flask**

**Objetivo:** En este laboratorio, aprenderás a construir una API sencilla utilizando el framework web Flask en Python. Flask es una herramienta popular para desarrollar aplicaciones web y APIs de manera rápida y sencilla. Aprenderás los conceptos básicos de cómo configurar rutas, manejar solicitudes HTTP y enviar respuestas JSON utilizando Flask.

**Paso 1: Configuración del entorno**
1. Asegúrate de tener Python instalado en tu sistema.
2. Instala Flask utilizando el siguiente comando:
   ```
   pip install Flask
   ```

**Paso 2: Creación de la aplicación Flask**
1. Crea una carpeta para tu proyecto y entra en ella desde la línea de comandos.
2. Crea un archivo llamado `app.py`.

**Paso 3: Esqueleto de la aplicación**
```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '¡Hola, mundo! Esta es mi primera API con Flask.'

if __name__ == '__main__':
    app.run()
```

**Paso 4: Ejecución de la aplicación**
1. Desde la línea de comandos, dentro de la carpeta de tu proyecto, ejecuta el siguiente comando:
   ```
   python app.py
   ```
2. Abre tu navegador y visita `http://localhost:5000/`. Deberías ver el mensaje "¡Hola, mundo!".

**Paso 5: Creación de una ruta con parámetros**
1. Modifica `app.py` para incluir una nueva ruta que acepte parámetros en la URL:
```python
@app.route('/saludo/<nombre>')
def saludar(nombre):
    return f'¡Hola, {nombre}! Bienvenido a mi API.'
```
2. Ejecuta la aplicación nuevamente y visita `http://localhost:5000/saludo/TuNombre`.

**Paso 6: Respuestas JSON**
1. Agrega una nueva ruta que devuelva una respuesta en formato JSON:
```python
@app.route('/json')
def json_response():
    data = {
        'mensaje': 'Esta es una respuesta JSON desde mi API.',
        'valor': 42
    }
    return jsonify(data)
```
2. No olvides importar `jsonify`:
```python
from flask import Flask, jsonify
```
3. Visita `http://localhost:5000/json` para ver la respuesta JSON.

**Paso 7: Métodos HTTP**
1. Modifica la ruta de saludo para aceptar diferentes métodos HTTP (GET y POST):
```python
@app.route('/saludo/<nombre>', methods=['GET', 'POST'])
def saludar(nombre):
    if request.method == 'GET':
        return f'¡Hola, {nombre}! Bienvenido a mi API.'
    elif request.method == 'POST':
        return f'Hola, {nombre}! Tu saludo ha sido enviado por POST.'
```
2. No olvides importar `request`:
```python
from flask import Flask, request
```

 Ahora aprenderás a crear una API en Flask que permita el registro (sign in) y el inicio de sesión (login) de usuarios utilizando un archivo JSON para almacenar la información de las cuentas. Aprenderás cómo manejar las rutas, los métodos HTTP y la gestión de sesiones básicas.

**Paso 8: Creación del archivo users**
1. Crea un archivo llamado `users.json` para almacenar la información de los usuarios en formato JSON.

**Paso 9: Contenido del archivo users.json**
```json
{
  "usuarios": [
    {
      "usuario": "usuario1",
      "contraseña": "clave123"
    },
    {
      "usuario": "usuario2",
      "contraseña": "abcd456"
    }
  ]
}
```

**Paso 10: Implementación de la API**
```python
from flask import Flask, request, jsonify

app = Flask(__name__)

# Ruta para el registro de usuarios
@app.route('/signup', methods=['POST'])
def sign_up():
    new_user = request.get_json()
    with open('users.json', 'r') as users_file:
        users_data = json.load(users_file)
    users_data['usuarios'].append(new_user)
    with open('users.json', 'w') as users_file:
        json.dump(users_data, users_file, indent=4)
    return jsonify({"message": "Usuario registrado exitosamente"})

# Ruta para el inicio de sesión
@app.route('/login', methods=['POST'])
def login():
    user_data = request.get_json()
    with open('users.json', 'r') as users_file:
        users_data = json.load(users_file)
    for user in users_data['usuarios']:
        if user['usuario'] == user_data['usuario'] and user['contraseña'] == user_data['contraseña']:
            return jsonify({"message": "Inicio de sesión exitoso"})
    return jsonify({"message": "Credenciales inválidas"})

if __name__ == '__main__':
    app.run()
```

**Paso 11: Ejecución de la aplicación**
1. Desde la línea de comandos, dentro de la carpeta de tu proyecto, ejecuta el siguiente comando:
   ```
   python app.py
   ```

**Paso 612 Prueba de la API**
1. Utiliza herramientas como `curl`, Postman o alguna librería de Python para hacer solicitudes HTTP.
2. Para registrar un usuario, realiza una solicitud POST a `http://localhost:5000/signup` con un cuerpo JSON que contenga el nombre de usuario y la contraseña.
3. Para iniciar sesión, realiza una solicitud POST a `http://localhost:5000/login` con un cuerpo JSON que contenga el nombre de usuario y la contraseña.

¡Felicidades! Has creado un laboratorio completo que combina los conceptos aprendidos para construir una API en Flask. Ahora tienes una API que permite el registro y el inicio de sesión de usuarios, así como una ruta de saludo con parámetros. A partir de aquí, puedes explorar más características y funcionalidades de Flask para seguir desarrollando tu API.