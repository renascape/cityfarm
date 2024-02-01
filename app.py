from flask import Flask, render_template
from flask_socketio import SocketIO
import setup
import threading
import time

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


@socketio.on('connect')
def test_connect():
    print('Client connected')


def background_thread():
    while True:
        socketio.emit('sensor_data', {'cur_time': setup.current_time(), 'DHT': setup.DHT_result()})
        time.sleep(1)


@app.route('/')
def index():
    thread = threading.Thread(target=background_thread)
    thread.daemon = True
    thread.start()
    return render_template('index.html')


if __name__ == '__main__':
    socketio.run(app, allow_unsafe_werkzeug=True)
