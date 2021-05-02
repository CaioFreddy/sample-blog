from flask import Flask
from api.views import bp
import os

app = Flask(__name__)
app.register_blueprint(bp)
os.environ['CASSANDRA_HOST'] = 'localhost'
os.environ['CASSANDRA_PORT'] = '9042'
os.environ['CASSANDRA_DBNAME'] = 'blog'


if __name__ == "__main__":
    app.run()