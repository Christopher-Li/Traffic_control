from gevent import monkey
monkey.patch_all()

from flask.ext.socketio import SocketIO, emit
from flask import Flask, render_template, url_for, copy_current_request_context
from random import random
from time import sleep
from threading import Thread, Event


app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.config['DEBUG'] = True

#turn the flask app into a socketio app
socketio = SocketIO(app)

@socketio.on('my event', namespace='/test')
def test_message(message):
    if message['data']['xAxis'] > 100:
        return None
    else:
        print message['data']['xAxis']

@app.route('/')
def index():
    #only by sending this page first will the client be connected to the socketio instance
    return render_template('index.html')

if __name__ == '__main__':
    socketio.run(app)