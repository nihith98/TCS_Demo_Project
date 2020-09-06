from flask import Flask, Markup
app = Flask(__name__)


@app.route("/")
def hello():
    return Markup('<h1 color="red">Hello World</h1>')

if __name__ == '__main__':
    app.run()