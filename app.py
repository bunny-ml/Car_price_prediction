from flask import Flask, render_template, request
import pickle
import json
import pandas as pd

app = Flask(__name__)

# model 
with open('/workspace/Car_price_prediction/random_forest_model.pkl' , 'rb') as file:
    model = pickle.load(file)

with open('/workspace/Car_price_prediction/options.json', 'r') as file:
    options = json.load(file)

@app.route('/')
def home():
    return render_template('car_index.html', options= options)

@app.route('/predict', methods=['POST'])
def prediction():
    # Example: simple logic for a "predicted price"
    present_price = float(request.form['present_price'])
    predicted_price = present_price * 0.8  # Example: dummy calculation
    return render_template('index.html', prediction=predicted_price)

if __name__ == '__main__':
    app.run(debug=True)
