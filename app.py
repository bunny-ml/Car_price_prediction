from flask import Flask, render_template, request
import pickle
import json
import pandas as pd

app = Flask(__name__)

# Load trained model
with open('/workspace/Car_price_prediction/random_forest_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Load options from JSON file
with open('/workspace/Car_price_prediction/options.json', 'r') as file:
    options = json.load(file)

@app.route('/')
def home():
    return render_template('car_index.html', options=options)

@app.route('/predict', methods=['POST'])
def prediction():
    try:
        present_price = float(request.form['present_price'])
        kms_driven = float(request.form['kms_driven'])
        owner = int(request.form['owner'])
        manufacturer = request.form['Manufacturer']
        model_name = request.form['Model']
        category = request.form['Category']
        leather_interior = request.form['Leather_interior']
        fuel_type = request.form['Fuel_type']
        engine_volume = float(request.form['Engine_volume'])
        mileage = float(request.form['Mileage'])
        cylinders = int(request.form['Cylinders'])
        gearbox_type = request.form['Gear_box_type']
        drive_wheels = request.form['Drive_wheels']
        wheel = request.form['Wheel']
        color = request.form['Color']
        airbags = int(request.form['Airbags'])
        car_age = int(request.form['car_age'])

        # Prepare input as a dataframe (modify based on model requirements)
        input_data = pd.DataFrame([[present_price, kms_driven, owner, manufacturer, model_name, category,
                                    leather_interior, fuel_type, engine_volume, mileage, cylinders,
                                    gearbox_type, drive_wheels, wheel, color, airbags, car_age]],
                                  columns=['Present_Price', 'Kms_Driven', 'Owner', 'Manufacturer', 'Model',
                                           'Category', 'Leather_interior', 'Fuel_type', 'Engine_volume',
                                           'Mileage', 'Cylinders', 'Gear_box_type', 'Drive_wheels',
                                           'Wheel', 'Color', 'Airbags', 'car_age'])

        # Predict car price
        predicted_price = model.predict(input_data)[0]

        return render_template('car_index.html', prediction=round(predicted_price, 2), options=options)

    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
