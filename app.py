from flask import Flask, render_template
from flask_socketio import SocketIO
import setup
import time

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


def background_thread():
    while True:
        time.sleep(1)
        current_time = setup.get_current_time()
        socketio.emit('time_update', {'time': current_time})


@socketio.on('connect', namespace='/time')
def connect():
    socketio.start_background_task(background_thread)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    socketio.run(app, debug=True, allow_unsafe_werkzeug=True)
