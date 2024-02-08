from flask import *
app = Flask(__name__)

@app.route('/', methods=['GET'])
def serve_index():
    return send_from_directory('static', 'index.html')

@app.route('/<path:path>', methods=['GET'])
def serve_static(path):
    return send_from_directory('static', path)

if __name__ == "__main__":
    app.run(threaded=True, port=5000)