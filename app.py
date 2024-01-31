from flask import Flask, render_template
from flask_socketio import SocketIO
import threading
import setup
import time

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


def update_time():
    while True:
        current_time = setup.current_time
        socketio.emit('update_time', {'time': current_time}, namespace='/time')
        time.sleep(1)


@app.route('/')
def index():
    return render_template('index.html')



if __name__ == '__main__':
    t = threading.Thread(target=update_time)
    t.start()
    socketio.run(app, debug=True, allow_unsafe_werkzeug=True)

