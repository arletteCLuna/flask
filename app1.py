from flask import Flask, request, render_template, jsonify
import pandas as pd
import joblib
import logging
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

app = Flask(__name__)

# Configurar el registro
logging.basicConfig(level=logging.DEBUG)

# Cargar el modelo entrenado
model = joblib.load('modelo1.pkl')
app.logger.debug('Modelo cargado correctamente.')
# Intentar cargar datos desde el CSV
try:
    data = pd.read_csv(model)
    app.logger.debug('Datos cargados correctamente.')
except FileNotFoundError as e:
    app.logger.error(f'Error al cargar los datos: {str(e)}')
    data = None

# Verifica que los datos fueron cargados correctamente
if data is not None:
    # Separar las características y la etiqueta
    X = data.drop('class', axis=1)
    y = data['class']
    
    # Dividir los datos en conjuntos de entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Entrenar el modelo
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    app.logger.debug('Modelo entrenado correctamente.')
else:
    model = None

@app.route('/')
def home():
    return render_template('formulario1.html')

@app.route('/predict', methods=['POST'])
def predict():
    if model is None:
        return jsonify({'error': 'Modelo no disponible'}), 500

    try:
        # Obtener los datos enviados en el request
        WBC = float(request.form['WBC'])
        RBC = float(request.form['RBC'])
        HGB = float(request.form['HGB'])
        MCV = float(request.form['MCV'])
        MCHC = float(request.form['MCHC'])
        PLT = float(request.form['PLT'])
        PCT = float(request.form['PCT'])
        
        # Crear un DataFrame con los datos
        data_df = pd.DataFrame([[WBC, RBC, HGB, MCV, MCHC, PLT, PCT]],
                               columns=['WBC', 'RBC', 'HGB', 'MCV', 'MCHC', 'PLT', 'PCT'])
        app.logger.debug(f'DataFrame creado: {data_df}')
        
        # Realizar predicciones
        prediction = model.predict(data_df)
        app.logger.debug(f'Predicción: {prediction[0]}')

        # Devolver las predicciones como respuesta JSON
        return jsonify({'Diagnosis': prediction[0]})
    except Exception as e:
        app.logger.error(f'Error en la predicción: {str(e)}')
        return jsonify({'error': str(e)}), 400
       
if __name__ == '__main__':
    app.run(debug=True)