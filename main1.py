from flask import Flask
from operator import *

app = Flask(__name__)
operations = ('+', ':', '**', '-', '*')
res = {'+': add, ':': truediv, '**': pow, '-': sub, '*': mul}


@app.route('/<int:a><o><int:b>/')
def test(a, b, o):
    return str(res[o](a, b))


if __name__ == '__main__':
    app.run(host='0.0.0.0.', port=5000)
