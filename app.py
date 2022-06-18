from flask import Flask
from flask import jsonify
# from flask import request

app = Flask(__name__)


@app.route('/')
def dummy_api():
    return jsonify(text_message = "Just print this in the local host (500)")


if __name__ == '__main__':
    app.run()