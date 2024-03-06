from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/index/')
def index():
    return 'index'


@app.route('/contact/')
def contact():
    return 'contact information'


@app.route('/calculate/<int:a>/<int:b>/')
def calculate(a, b):
    return str(a ** b)


if __name__ == '__main__':
    app.run(host='0.0.0.0.', port=8080)
