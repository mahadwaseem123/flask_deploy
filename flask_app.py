
from flask import Flask

import url_marker

app = Flask(__name__)


@app.route("/")
def index():
    return '<h1>deployed!!!</h1>'

if __name__ == "__main__":
    app.run()
