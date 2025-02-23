from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

# Load the trained model
with open('random_forest_model.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/')
def home():
    return render_template('car_index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get features from the form
    features = [float(request.form['present_price']),
                float(request.form['kms_driven']),
                int(request.form['owner']),
                int(request.form['fuel_type']),
                int(request.form['seller_type']),
                int(request.form['transmission']),
                int(request.form['year'])]

    # Convert features to DataFrame
    features_df = pd.DataFrame([features], columns=['Present_Price', 'Kms_Driven', 'Owner', 'Fuel_Type', 'Seller_Type', 'Transmission', 'Year'])

    # Make prediction
    prediction = model.predict(features_df)
    return render_template('car_index.html', prediction=prediction[0])

if __name__ == '__main__':
    app.run(debug=True)