from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "<h1> link del coso este </h1>"


if __name__ == "_main_":
    app.run(debug=True)
