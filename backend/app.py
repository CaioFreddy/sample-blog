from flask import Flask
from api.views import bp
import os

app = Flask(__name__)
app.register_blueprint(bp)

if __name__ == "__main__":
    app.run()
