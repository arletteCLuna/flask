from flask import Flask, request

app = Flask(__name__)

# Página principal con un formulario para ingresar el radio
@app.route('/')
def home():
    return '''
        <html>
            <head>
                <style>
                    body {
                        font-family: Arial, sans-serif;
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        height: 100vh;
                        background-color: #f0f8ff;
                        margin: 0;
                    }
                    .container {
                        text-align: center;
                        padding: 20px;
                        border: 1px solid #ccc;
                        border-radius: 10px;
                        background-color: #fff;
                        box-shadow: 0 0 10px rgba(0,0,0,0.1);
                    }
                    input[type="number"] {
                        margin: 10px 0;
                        padding: 10px;
                        width: calc(100% - 22px);
                        border: 1px solid #ccc;
                        border-radius: 5px;
                    }
                    input[type="submit"] {
                        padding: 10px 20px;
                        border: none;
                        border-radius: 5px;
                        background-color: #800080;
                        color: white;
                        cursor: pointer;
                    }
                    input[type="submit"]:hover {
                        background-color: #4B0082;
                    }
                    img {
                        width: 150px;
                        height: auto;
                        margin-top: 20px;
                    }
                </style>
            </head>
            <body>
                <div class="container">
                <h2>ARLETTE CRUZ LUNA - 9B</h2>
                    <h2>Calculadora - Área y Perímetro de un Círculo</h2>
                    <img src="https://www.decagono.com/img/circulo-radio.png" alt="Círculo">
                    <form action="/calcular" method="post">
                        <label for="radio">Ingresa el radio:</label>
                        <input type="number" id="radio" name="radio" step="any" required>
                        <br>
                        <input type="submit" value="Calcular">
                    </form>
                    
                </div>
            </body>
        </html>
    '''

# Ruta para calcular el área y el perímetro del círculo
@app.route('/calcular', methods=['POST'])
def calcular():
    radio = float(request.form['radio'])
    area = 3.1416 * (radio ** 2)
    perimetro = 2 * 3.1416 * radio
    return f'''
        <html>
            <head>
                <style>
                    body {{
                        font-family: Arial, sans-serif;
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        height: 100vh;
                        background-color: #f0f8ff;
                        margin: 0;
                    }}
                    .container {{
                        text-align: center;
                        padding: 20px;
                        border: 1px solid #ccc;
                        border-radius: 10px;
                        background-color: #fff;
                        box-shadow: 0 0 10px rgba(0,0,0,0.1);
                    }}
                    a {{
                        display: inline-block;
                        margin-top: 20px;
                        padding: 10px 20px;
                        border: none;
                        border-radius: 5px;
                        background-color: #800080;
                        color: white;
                        text-decoration: none;
                    }}
                    a:hover {{
                        background-color: #4B0082;
                    }}
                </style>
            </head>
            <body>
                <div class="container">
                    <h2>Resultados</h2>
                    <p>Radio: {radio}</p>
                    <p>Área del círculo: {area}</p>
                    <p>Perímetro del círculo: {perimetro}</p>
                    <a href="/">Calcular otra vez</a>
                </div>
            </body>
        </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)
