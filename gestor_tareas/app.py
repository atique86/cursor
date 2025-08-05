from flask import Flask, request, redirect, render_template
import json
import os

app = Flask(__name__)

# Archivo para persistencia
TAREAS_FILE = 'tareas.json'

# Lista global de tareas
tareas = []
id_contador = 1

def cargar_tareas():
    global tareas, id_contador
    if os.path.exists(TAREAS_FILE):
        try:
            with open(TAREAS_FILE, 'r', encoding='utf-8') as f:
                data = json.load(f)
                tareas = data.get('tareas', [])
                id_contador = data.get('id_contador', 1)
        except:
            tareas = []
            id_contador = 1

def guardar_tareas():
    data = {
        'tareas': tareas,
        'id_contador': id_contador
    }
    with open(TAREAS_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def agregar_tarea(texto):
    global id_contador
    tarea = {
        'id': id_contador,
        'texto': texto,
        'completada': False
    }
    tareas.append(tarea)
    id_contador += 1
    guardar_tareas()
    return tarea

def completar_tarea(id):
    for tarea in tareas:
        if tarea['id'] == id:
            tarea['completada'] = True
            guardar_tareas()
            return tarea
    return None

def eliminar_tarea(id):
    global tareas
    tareas = [t for t in tareas if t['id'] != id]
    guardar_tareas()

def editar_tarea(id, nuevo_texto):
    for tarea in tareas:
        if tarea['id'] == id:
            tarea['texto'] = nuevo_texto
            guardar_tareas()
            return tarea
    return None

# Cargar tareas al iniciar
cargar_tareas()

# Rutas de la aplicación
@app.route('/tareas')
def listar_tareas():
    return {'tareas': tareas}

@app.route('/tareas', methods=['POST'])
def crear_tarea():
    data = request.get_json()
    if not data or 'texto' not in data:
        return {'error': 'Se requiere el campo "texto"'}, 400
    
    nueva_tarea = agregar_tarea(data['texto'])
    return nueva_tarea, 201

@app.route('/tareas/<int:id>/completar')
def marcar_completada(id):
    tarea = completar_tarea(id)
    if tarea:
        return tarea
    return {'error': 'Tarea no encontrada'}, 404

@app.route('/tareas/<int:id>/eliminar', methods=['POST'])
def eliminar_tarea_route(id):
    eliminar_tarea(id)
    return {'message': 'Tarea eliminada'}

@app.route('/tareas/<int:id>/editar', methods=['POST'])
def editar_tarea_route(id):
    data = request.get_json()
    if 'nuevo_texto' not in data:
        return {'error': 'Se requiere el campo "nuevo_texto"'}, 400
    tarea_editada = editar_tarea(id, data['nuevo_texto'])
    if tarea_editada:
        return tarea_editada
    return {'error': 'Tarea no encontrada'}, 404

@app.route('/eliminar/<int:id>')
def eliminar(id):
    eliminar_tarea(id)
    return redirect('/')

@app.route('/editar/<int:id>', methods=['POST'])
def editar(id):
    nuevo_texto = request.form.get('nuevo_texto')
    if nuevo_texto:
        editar_tarea(id, nuevo_texto)
    return redirect('/')

@app.route('/completar/<int:id>')
def completar(id):
    completar_tarea(id)
    return redirect('/')

@app.route('/agregar', methods=['POST'])
def agregar():
    texto_tarea = request.form.get('texto_tarea')
    if texto_tarea:
        agregar_tarea(texto_tarea)
    return redirect('/')

@app.route('/')
def index():
    # Ordenar tareas: incompletas primero, luego completadas
    tareas_ordenadas = sorted(tareas, key=lambda t: t['completada'])
    return render_template('index.html', tareas=tareas_ordenadas)


if __name__ == '__main__':
    app.run(debug=True)
