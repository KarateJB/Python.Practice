from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, send, emit
import json


app = Flask(__name__, template_folder='./templates')

# Websocket setting
app.config['SECRET_KEY'] = '12qwaszx'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')    

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

@socketio.on('connect_event')
def connected_event(msg):
    """WebSocket connect event
    This will trigger responsing a message to client by 
    """
    print('Received msg: %s', msg)
    emit('server_response', {'data': msg['data']})

if __name__=='__main__':
    socketio.run(app)
