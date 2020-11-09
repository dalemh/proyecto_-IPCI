from flask import (     Flask,        redirect,    render_template, jsonify,
                         request,     session,     url_for
)
from flask_cors import CORS
from user import cliente
from songs import cancion


users = []
canciones = []

canciones.append(cancion(id=1, cancion="Maniac", artista="Michael Sambelo", album="Flashdance", fecha="1983",imagen="https://i.musicaimg.com/letras/max/67021.jpg", spotify="https://open.spotify.com/embed/track/0QKfiqpEU4h9ycPSzIFwYe", video="https://www.youtube.com/embed/qvYQ1TNbf2g"))

users.append(cliente(id=1,nombre='Usuario',apellido='Maestro',usuario='admin', password='admin',admin='Administrador'))
users.append(cliente(id=2, nombre='Becca',apellido='Pérez',usuario='user1', password='secret',admin='Cliente'))

app = Flask(__name__)
CORS(app)

        

@app.route('/login', methods=['POST'])
def Login():
    global users
    username = request.json['usuario']
    password = request.json['password']
    for usuario in users:
        if usuario.getUsuario() == username and usuario.getPassword() == password:
            Dato = {
                'message': 'se ha realizado con éxito',
                'usuario': usuario.getUsuario(),
                'tipo': usuario.getAdmin()
                }
            break
        else:
            Dato = {
                'message': 'incorrecto',
                'usuario': ''
            }
    respuesta = jsonify(Dato)
    return(respuesta)


@app.route('/registrar', methods=['POST'])
def AgregarUsuario():
    global users
    identificador = len(users)+1
    nombre = request.json['nombre']
    apellido = request.json['apellido']
    username = request.json['usuario']
    password = request.json['password']
    admin='Cliente'
    encontrado = False
    for usuario in users:
        if usuario.getUsuario() == username:
            encontrado = True
            break
    if encontrado:
        return jsonify({
            'message':'fallo',
            'reason':'El usuario ya esta registrado'
            })
    else:
        nuevo = cliente(identificador, nombre,apellido,username,password,admin)
        users.append(nuevo)
        return jsonify({
            'message':'exito',
            'reason':'Se agrego el usuario'
            })

@app.route('/buscarc', methods=['POST'])
def buscarusers():
    global users
    username = request.json['usuario']
    encontrado = False
    for usuario in users:
        if usuario.getUsuario() == username:
            encontrado = True
            break
    if encontrado:
        return jsonify({
            'message':'exito',
            'password':usuario.getPassword()
            })
    else:
        return jsonify({
            'message':'fallo'
            })
    
@app.route('/cancion', methods=['POST'])
def guardarCancion():
    global canciones 
    id = len(canciones)+1
    nombre = request.json['nombre']
    artista = request.json['artista']
    album = request.json['album']
    fecha = request.json['fecha']
    imagen = request.json['imagen']
    spotify = request.json['spotify']
    video = request.json['video']
    nuevo = cancion(id, nombre, artista, album, fecha, imagen, spotify, video)
    canciones.append(nuevo)
    return jsonify({
            'message':'Success',
            'reason':'Se agrego la cancion'
            })

@app.route('/cancion', methods=['GET'])
def obtenerCanciones():
    global canciones
    Datos = []
    for cancion in canciones:
        Dato = {
            'id': cancion.getId(),
            'nombre': cancion.getCancion(),
            'artista': cancion.getArtista(),
            'album': cancion.getAlbum(),
            'fecha': cancion.getFecha(),
            'imagen': cancion.getImagen(),
            'spotify': cancion.getSpotify(),
            'video': cancion.getVideo()     
            }
        Datos.append(Dato)
    respuesta = jsonify(Datos)
    return(respuesta)

if __name__ == "__main__":
    app.run(threaded=True, host="0.0.0.0",port=5000, debug=True)