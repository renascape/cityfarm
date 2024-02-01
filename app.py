from flask import Flask, render_template
from flask_socketio import SocketIO
import setup
import threading
import time

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


current_thread = None


@socketio.on('connect')
def test_connect():
    print('Client connected')


def background_thread():
    while True:
        socketio.emit('sensor_data', {'cur_time': setup.current_time(), 'DHT': setup.DHT_result()})
        time.sleep(1)


@app.before_request
def activate_job():
    global current_thread
    if current_thread is None or not current_thread.is_alive():
        current_thread = threading.Thread(target=background_thread)
        current_thread.start()


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    socketio.run(app, allow_unsafe_werkzeug=True)
