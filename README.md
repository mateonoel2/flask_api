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

¡Felicidades! Has creado tu primer laboratorio para construir una API con Flask. Este lab te proporciona una introducción básica a Flask y cómo crear rutas, manejar solicitudes HTTP y enviar respuestas JSON. A partir de aquí, puedes explorar más funciones y características de Flask para desarrollar APIs más complejas y robustas.