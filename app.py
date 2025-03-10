from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('car_index.html')

@app.route('/predict', methods=['POST'])
def prediction():
    # Example: simple logic for a "predicted price"
    present_price = float(request.form['present_price'])
    predicted_price = present_price * 0.8  # Example: dummy calculation
    return render_template('index.html', prediction=predicted_price)

if __name__ == '__main__':
    app.run(debug=True)
