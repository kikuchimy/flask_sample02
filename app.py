from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello World!"


@app.route("/owner")
def owner():
    return "Hello Owner"


@app.route("/member")
def member():
    return "Hello Member"


if __name__ == "__main__":
    app.run()
    # app.run(debug=True)
