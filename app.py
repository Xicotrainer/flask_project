from flask import Flask

app = Flask(__name__)


@app.route('/')
def dummy_api():
    return("Hello moto... desde flask calnal")


if __name__ == "__main__":
    app.run()