from flask import Flask
from flask_cors import CORS
from routes import main_bp

app = Flask(__name__)
CORS(app)  # Enable CORS

app.register_blueprint(main_bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
