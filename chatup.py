from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit
from googletrans import Translator
import googletrans


# https://flask-socketio.readthedocs.io/en/latest/
# https://github.com/socketio/socket.io-client

app = Flask(__name__)

app.config[ 'SECRET_KEY' ] = 'jsbcfsbfjefebw237u3gdbdc'
socketio = SocketIO( app )

translator = Translator()

@app.route( '/' )
def hello():
  return render_template('./ChatApp.html')


def messageRecived():
  print( 'message was received!!!' )

# asdsad
@socketio.on( 'my event' )
def handle_my_custom_event( json ):
  if('message' in json):
    result = translator.translate(json['message'])
    json['message'] = result.text
    json['source'] = googletrans.LANGUAGES[result.src.lower()]
    print( 'recived my event: ' + str( json ) )
  socketio.emit( 'my response', json, callback=messageRecived )


if __name__ == '__main__':
  socketio.run( app, debug = True )


