from flask import *
from flask.ext.socketio import SocketIO, send, emit
import json, sys
import os

from src import model

# Configuration du framework
DEBUG = True

# Initialisation du framework
app = Flask(__name__, static_url_path='/static')
app.config.from_object(__name__)
app.config['SECRET_KEY'] = 'top_chretien_map_monde'
socketio = SocketIO(app)


model = model.MapModel()

# Vue principale pour le rendu de la page
@app.route('/')
def main():
	return render_template('map.html', model=model)


@socketio.on('init_session', namespace='/api')
def initialize(message):
    user = model.addUser(message)
    emit('new_user', user, broadcast=True)


@socketio.on('get_users', namespace='/api')
def sendUsers():
	emit('pull_users', model.getUsersConnected())


#@socketio.on('set.servo.y', namespace='/api')
#def setServoXAxis(message):
#	model.setYAxis(meesage['yaxis'])

#@socketio.on('set.servos', namespace='/api')
#def setServoXAxis(message):
#	model.setXAxis(message['xaxis'])
#	model.setYAxis(message['yaxis'])
#	emit('get_servos_evt', {'xaxis': model.getXAxis(), 'yaxis': model.getYAxis() }, broadcast=True)
#
#@socketio.on('get.servos', namespace='/api')
#def getServos():
#	emit('get_servos_evt', {'xaxis': model.getXAxis(), 'yaxis': model.getYAxis() }, broadcast=True)
#
#@socketio.on('get.videoconf', namespace='/api')
#def getVideoConf():
#	emit('get_videoconf_evt', {'ipadress': model.ipadress, 'port': model.port, 'uri': model.uri})
#
#@socketio.on('playsound', namespace='/api')
#def target(message):
#	emit('played_sound', message['what'] + ".mp3", broadcast=True)
#	os.system("python PlaySound.py " + message['what'])
#
#@socketio.on('playrandomway', namespace='/api')
#def target(message):
#	model.playRandomWay(message['directions'])
#	emit('get_servos_evt', {'xaxis': model.getXAxis(), 'yaxis': model.getYAxis() }, broadcast=True)
#

# Demarrage du framework
if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0')
