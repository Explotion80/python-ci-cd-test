from flask import Flask, render_template, request

app = Flask(__name__)

def add(a, b):
    return a + b

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', result=None, a=None, b=None)

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        a = float(request.form['a'])
        b = float(request.form['b'])
        result = add(a, b)
        return render_template('index.html', result=result, a=a, b=b)
    except ValueError:
        return render_template('index.html', result="Invalid input", a=None, b=None)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)