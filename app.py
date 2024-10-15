# import os
# from flask import Flask, render_template, request, jsonify
# from flask_restful import Api, Resource
# import joblib
# import numpy as np

# app = Flask(__name__)
# api = Api(app)

# # Obtener la ruta absoluta al directorio actual
# basedir = os.path.abspath(os.path.dirname(__file__))

# # Construir la ruta completa al modelo
# model_path = os.path.join(basedir, 'model', 'heart_disease_model.pkl')

# # Verificar si el archivo del modelo existe
# if not os.path.exists(model_path):
#     raise FileNotFoundError(f"No se encontró el archivo del modelo en {model_path}")

# # Cargar el modelo
# try:
#     model = joblib.load(model_path)
#     print("Modelo cargado exitosamente.")
# except Exception as e:
#     print(f"Error al cargar el modelo: {e}")
#     model = None

# # Ruta principal para el formulario HTML
# @app.route('/')
# def index():
#     return render_template('index.html')

# # Ruta para manejar la predicción desde el formulario HTML
# @app.route('/predict', methods=['POST'])
# def predict():
#     if model is None:
#         return "Modelo no cargado correctamente.", 500
#     try:
#         # Obtener datos del formulario
#         data = request.form.to_dict()
#         # Convertir los datos a float
#         input_data = [float(data[key]) for key in data]
#         input_array = np.array(input_data).reshape(1, -1)
#         # Realizar la predicción
#         prediction = model.predict(input_array)
#         # Interpretar el resultado
#         result = 'Enfermedad del Corazón' if prediction[0] == 1 else 'No Enfermedad del Corazón'
#         return render_template('index.html', prediction=result)
#     except Exception as e:
#         return f"Error al realizar la predicción: {e}", 400


# # Definir el recurso para la API RESTful
# class PredictAPI(Resource):
#     def post(self):
#         if model is None:
#             return {'error': 'Modelo no cargado correctamente.'}, 500
#         try:
#             json_data = request.get_json(force=True)
#             # Asegúrate de que los campos estén en el orden correcto
#             input_data = [
#                 float(json_data['age']),
#                 float(json_data['sex']),
#                 float(json_data['cp']),
#                 float(json_data['trestbps']),
#                 float(json_data['chol']),
#                 float(json_data['fbs']),
#                 float(json_data['restecg']),
#                 float(json_data['thalach']),
#                 float(json_data['exang']),
#                 float(json_data['oldpeak']),
#                 float(json_data['slope']),
#                 float(json_data['ca']),
#                 float(json_data['thal'])
#             ]
#             input_array = np.array(input_data).reshape(1, -1)
#             prediction = model.predict(input_array)
#             result = int(prediction[0])
#             return jsonify({'prediction': result})
#         except Exception as e:
#             return {'error': str(e)}, 400

# # Añadir el recurso a la API
# api.add_resource(PredictAPI, '/api/predict')

# if __name__ == '__main__':
#     app.run(debug=True)
import os
from flask import Flask, render_template, request, jsonify
from flask_restful import Api, Resource
import joblib
import numpy as np
import pandas as pd

app = Flask(__name__)
api = Api(app)

# Obtener la ruta absoluta al directorio actual
basedir = os.path.abspath(os.path.dirname(__file__))

# Construir la ruta completa al modelo
model_path = os.path.join(basedir, 'model', 'heart_disease_model.pkl')

# Verificar si el archivo del modelo existe
if not os.path.exists(model_path):
    raise FileNotFoundError(f"No se encontró el archivo del modelo en {model_path}")

# Cargar el modelo
try:
    model = joblib.load(model_path)
    print("Modelo cargado exitosamente.")
except Exception as e:
    print(f"Error al cargar el modelo: {e}")
    model = None

# Ruta principal para el formulario HTML
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para manejar la predicción desde el formulario HTML
@app.route('/predict', methods=['POST'])
def predict():
    # Obtener los datos del formulario
    data = {
        'age': float(request.form.get('age')),
        'trestbps': float(request.form.get('trestbps')),
        'chol': float(request.form.get('chol')),
        'thalach': float(request.form.get('thalach')),
        'oldpeak': float(request.form.get('oldpeak')),
        'sex_male': float(request.form.get('sex')),
        'cp_atypical angina': 1 if request.form.get('cp') == '2' else 0,
        'cp_non-anginal pain': 1 if request.form.get('cp') == '1' else 0,
        'cp_typical angina': 1 if request.form.get('cp') == '0' else 0,
        'fbs_1': float(request.form.get('fbs')),
        'restecg_1': 1 if request.form.get('restecg') == '1' else 0,
        'restecg_2': 1 if request.form.get('restecg') == '2' else 0,
        'exang_1': float(request.form.get('exang')),
        'slope_2': 1 if request.form.get('slope') == '1' else 0,
        'slope_3': 1 if request.form.get('slope') == '2' else 0,
        'ca_0.6722408026755853': 1 if request.form.get('ca') == '0' else 0,
        'ca_1.0': 1 if request.form.get('ca') == '1' else 0,
        'ca_2.0': 1 if request.form.get('ca') == '2' else 0,
        'ca_3.0': 1 if request.form.get('ca') == '3' else 0,
        'thal_4.73421926910299': 1 if request.form.get('thal') == '4' else 0,
        'thal_6.0': 1 if request.form.get('thal') == '6' else 0,
        'thal_7.0': 1 if request.form.get('thal') == '7' else 0
    }
    
    # Crear un DataFrame con los datos (sin incluir 'target')
    input_data = pd.DataFrame(data, index=[0])
    
    # Verificar las columnas
    print("Datos de entrada:", input_data)

    # Realizar la predicción
    prediction = model.predict(input_data)
    
    # Devolver el resultado
    return f'Predicción: {"Heart disease" if prediction[0] == 1 else "No heart disease"}'



# Definir el recurso para la API RESTful
class PredictAPI(Resource):
    def post(self):
        if model is None:
            return {'error': 'Modelo no cargado correctamente.'}, 500
        try:
            json_data = request.get_json(force=True)
            # Asegúrate de que los campos estén en el orden correcto
            input_data = [
                float(json_data['age']),
                float(json_data['sex']),
                float(json_data['cp']),
                float(json_data['trestbps']),
                float(json_data['chol']),
                float(json_data['fbs']),
                float(json_data['restecg']),
                float(json_data['thalach']),
                float(json_data['exang']),
                float(json_data['oldpeak']),
                float(json_data['slope']),
                float(json_data['ca']),
                float(json_data['thal'])
            ]
            input_array = np.array(input_data).reshape(1, -1)
            prediction = model.predict(input_array)
            result = int(prediction[0])
            return jsonify({'prediction': result})
        except Exception as e:
            return {'error': str(e)}, 400

# Añadir el recurso a la API
api.add_resource(PredictAPI, '/api/predict')
if __name__ == '__main__':
    app.run(debug=True)