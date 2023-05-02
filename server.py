from flask import Flask, request, jsonify , render_template
import joblib

app = Flask(__name__)

# Carga el modelo desde el archivo
model = joblib.load('model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def predict():
    print(request.form)
   # obtener el valor del formulario
    celsius = float(request.form['celsius'])
    print(celsius)
    # hacer la predicción con el modelo
    fahrenheit = model.predict([[celsius]])[0][0]
    print(fahrenheit)
    # redondear la respuesta a dos decimales
    fahrenheit = round(fahrenheit, 2)
    print(fahrenheit)
    # mostrar el resultado
    return '{} grados Celsius son {} grados Fahrenheit'.format(celsius, fahrenheit)

if __name__ == '__main__':
    app.run()