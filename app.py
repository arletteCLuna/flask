from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
        return "Hola mundo - Arlette Cruz Luna 9B :)"

if __name__ == '__main__':
        app.run(debug=True)