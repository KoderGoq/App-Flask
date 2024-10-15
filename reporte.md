# Reporte: Aplicación Web para Predicción de Enfermedades Cardíacas

## Proceso de desarrollo

1. Preparación del entorno:
   - Instalamos las dependencias necesarias: Flask, numpy, pandas, scikit-learn.
   - Creamos un archivo `requirements.txt` para facilitar la instalación de dependencias.

2. Desarrollo de la aplicación Flask:
   - Creamos `app.py` como el punto de entrada de nuestra aplicación.
   - Implementamos la lógica para cargar datos, entrenar el modelo y hacer predicciones.

3. Guardado y carga del modelo:
   - Utilizamos `joblib` para guardar el modelo entrenado y el scaler en archivos separados.
   - Modificamos `app.py` para cargar el modelo y el scaler al inicio de la aplicación.

4. Creación de la interfaz de usuario:
   - Desarrollamos `index.html` en la carpeta `templates` para crear un formulario dinámico.
   - El formulario se genera automáticamente basado en las características del dataset.

5. Despliegue de la aplicación:
   - Ejecutamos la aplicación localmente usando el servidor de desarrollo de Flask.

## Capturas de pantalla

[Aquí deberías incluir capturas de pantalla mostrando la aplicación en funcionamiento]

## Instrucciones para ejecutar la aplicación

1. Asegúrate de tener Python instalado en tu sistema.
2. Instala las dependencias ejecutando: `pip install -r requirements.txt`
3. Ejecuta la aplicación con: `python app.py`
4. Abre un navegador y ve a `http://127.0.0.1:5000/`

## Archivos del proyecto

- `app.py`: Contiene la lógica principal de la aplicación Flask.
- `heart_disease_model.pkl`: Modelo de Random Forest guardado.
- `scaler.pkl`: Objeto StandardScaler guardado.
- `templates/index.html`: Plantilla HTML para la interfaz de usuario.
- `requirements.txt`: Lista de dependencias del proyecto.
- `heart_disease_examen.csv`: Dataset utilizado para entrenar el modelo.

## Conclusión

Esta aplicación web demuestra cómo se puede implementar un modelo de machine learning en una interfaz web simple utilizando Flask. La aplicación permite a los usuarios ingresar datos de salud y obtener una predicción sobre la posibilidad de enfermedad cardíaca.