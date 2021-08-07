from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)

app.config['SECRET_KEY'] = 'superDuperSecretKey'
socketio = SocketIO(app)

@app.route('/')
def index():
  return render_template('./index.html')

def messageRecived():
  print('message received!!!')

@socketio.on('my event')
def handle_my_custom_event( json ):
  print('recived my event: ' + str( json ))
  socketio.emit('my response', json, callback=messageRecived)

if __name__ == '__main__':
  app.run()