from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit
app = Flask(__name__, template_folder='./templates')

# Websocket setting
app.config['SECRET_KEY'] = '12qwaszx'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')    


# @app.route('/<string:page_name>/')
# def static_page(page_name):
#     return render_template('%s.html' % page_name)    

@socketio.on('message')
def handle_message(message):
    print('received message: ' + message)    

@socketio.on('connect_event')
def connected_event(msg):
    print('Received msg: %s', msg)
    emit('server_response', {'data': msg['data']}, broadcast=True)

@socketio.on('save receipt')
def handle_json(json):
    print('Received json: ' + str(json))
    emit('save-reveipt response', {'isSuccess': 'true'})

if __name__=='__main__':
    socketio.run(app)
