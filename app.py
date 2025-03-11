from flask import Flask, render_template, request
import pickle
import json
import pandas as pd

app = Flask(__name__)

@app.route('/test')
def test():
    return "Test route working!"


# Load the pickled label encoders
with open('label_encoders.pkl', 'rb') as file:
    label_encoders = pickle.load(file)

# Load trained model
with open('/workspace/Car_price_prediction/random_forest_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Load options from JSON file
with open('/workspace/Car_price_prediction/options.json', 'r') as file:
    options = json.load(file)

@app.route('/')
def home():
    print("Home route accessed")
    return render_template('car_index.html', options=options)

@app.route('/predict', methods=['POST'])
def prediction():
    try:
        # Get user inputs from form
        data = {
            'Manufacturer': request.form['Manufacturer'],
            'Model': request.form['Model'],
            'Prod_year': int(request.form['Prod_year']),
            'Category': request.form['Category'],
            'Leather_interior': request.form['Leather_interior'],
            'Fuel_type': request.form['Fuel_type'],
            'Engine_volume': float(request.form['Engine_volume']),
            'Mileage': float(request.form['Mileage']),
            'Cylinders': int(request.form['Cylinders']),
            'Gear_box_type': request.form['Gear_box_type'],
            'Drive_wheels': request.form['Drive_wheels'],
            'Wheel': request.form['Wheel'],
            'Color': request.form['Color'],
            'Airbags': int(request.form['Airbags']),
            'car_age': int(request.form['car_age'])
        }

        print("Data received:", data)
        
        # Convert to DataFrame (model expects input in DataFrame format)
        input_df = pd.DataFrame([data])

        # Ensure correct column order for model input
        df = input_df[['Manufacturer', 'Model', 'Prod_year', 'Category', 'Leather_interior',
                             'Fuel_type', 'Engine_volume', 'Mileage', 'Cylinders', 'Gear_box_type',
                             'Drive_wheels', 'Wheel', 'Color', 'Airbags', 'car_age']]

          # Encode categorical variables (with error handling for unseen labels)
        for col, encoder in label_encoders.items():
            if col in df.columns:
                try:
                    df[col] = encoder.transform(df[col])
                except ValueError:
                    df[col] = -1  # Assign unknown labels a default value (-1)

        
        # Make prediction
        prediction = model.predict(df)[0]
        predicted_price = round(prediction, 2)
        
        return render_template('car_index.html', options=options, prediction=f"${predicted_price}")
    
    
    except Exception as e:
        print(f"Error: {e}")
        return render_template('car_index.html', options=options, error="An error occurred during prediction.")


if __name__ == '__main__':
    app.run(debug=True)
