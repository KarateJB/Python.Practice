from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, send, emit
from modules.logger_config import init_logging
import modules.config as config
import modules.sqlalchemy_config as sqlalchemy_config
import json
import logging

# Global variables
SERVER_ADDR = "http://localhost:5000"  # default Server ip/port (local)

class CustomFlask(Flask):
    jinja_options = Flask.jinja_options.copy()
    jinja_options.update(dict(
        # Default is '{{' but Vue.js uses '{{' / '}}'
        variable_start_string='%%',
        # Default is '}}' but Vue.js uses '{{' / '}}'
        variable_end_string='%%',
    ))


app = CustomFlask(__name__, template_folder='./templates')
# app = Flask(__name__, template_folder='./templates')
app.config.from_object(config.TestConfig)


# Initilize db 
with app.app_context():
    db = sqlalchemy_config.db = sqlalchemy_config.init_db()
    
from models import user, product, order
from models.user import *
from models.product import *
from models.order import *
migrate = sqlalchemy_config.migrate_db(app, db)


# Logging setting
flask_logger = logging.getLogger("flask")
if(app.debug == False):  # When not in development env
    # Set app.logger's logLevel > 50(CRITICAL) => Disable application-level logging
    init_logging(app.logger, 9999)
    init_logging(flask_logger, logging.INFO)
else:  # When in local env
    init_logging(app.logger, logging.DEBUG)
    init_logging(flask_logger, logging.DEBUG)


# Websocket setting
app.config['SECRET_KEY'] = '12qwaszx'
socketio = SocketIO(app)


@app.route("/")
def index():
    # For jquery + Socket.IO client
    # return render_template('index.html', async_mode=socketio.async_mode)
    # For Vuejs + Vue-SocketIO
    return render_template('index_vue.html', async_mode=socketio.async_mode, server_addr=SERVER_ADDR)


@app.route("/create-user", methods=["POST"])
def create_user():
    json_obj = request.json
    entity = User(**json_obj)
    User.create(entity)
    return "", 201

@app.route("/update-user", methods=["POST"])
def update_user():
    json_obj = request.json
    id = json_obj["id"]
    entity = User.query.filter_by(id=id).first()
    entity.name = json_obj["name"]
    entity.phone = json_obj["phone"]
    User.update(entity)
    return "", 200    

@app.route("/delete-user", methods=["DELETE"])
def delete_user():
    json_obj = request.json
    id = json_obj["id"]
    entity = User.query.filter_by(id=id).first()
    User.delete(entity)
    return "", 200    

@app.route("/send", methods=['GET', 'POST'])
def send():
    """Receive a message and brodcast to all connected clients
    """
    jsonobj_content = request.json
    flask_logger.debug("Received: {0}".format(jsonobj_content))
    socketio.emit('server_response',  {
                  'data': str(jsonobj_content)}, broadcast=True)
    return "", 200


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
    flask_logger.debug("Broadcasting: {0}".format(msg))
    app.logger.debug("Broadcasting: {0}".format(msg))
    emit('server_response', {'data': msg['data']}, broadcast=True)


@app.route('/shutdown', methods=['GET'])
def shutdown():
    """Shutdown flask-socketio
    """
    flask_logger.info("Server shutting down...")
    socketio.stop()
    return 'Server is down'  # This line is useless since the service is down


if __name__ == '__main__':
    app.logger.info("Flask is running on {0}".format(str(SERVER_ADDR)))
    socketio.run(app, host='0.0.0.0', port=5000)
    socketio.run(app)
