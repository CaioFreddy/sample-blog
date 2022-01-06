from flask import Flask
from flask_cors import CORS
from api.views import bp
import os

app = Flask(__name__)
app.register_blueprint(bp)
CORS(app)

if __name__ == "__main__":
    app.run()
