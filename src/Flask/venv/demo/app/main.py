from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, send, emit
import json


app = Flask(__name__, template_folder='./templates')

# Websocket setting
app.config['SECRET_KEY'] = '12qwaszx'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html', async_mode=socketio.async_mode)    

@app.route('/send', methods=['GET', 'POST'])
def send():
    """Receive a message and brodcast to all connected clients
    """
    jsonobj_content = request.json
    socketio.emit('server_response',  {'data':str(jsonobj_content)}, broadcast=True)
    return '', 200


# @app.route('/<string:page_name>/')
# def static_page(page_name):
#     return render_template('%s.html' % page_name)    

@socketio.on('connected_event')
def connected(msg):
    """WebSocket connect event
    This will trigger responsing a message to client
    """
    emit('server_response', {'data': msg['data']})

@socketio.on('broadcast_event')
def broadcast(msg):
    print(msg)
    emit('server_response', {'data': msg['data']}, broadcast=True)


if __name__=='__main__':
    socketio.run(app)
