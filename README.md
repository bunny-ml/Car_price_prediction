# Car Price Prediction

A machine learning project that predicts car prices using a Random Forest model. The model has been trained and evaluated, achieving an accuracy of 78%.

## Table of Contents
- [Introduction](#introduction)
- [Technologies Used](#technologies-used)
- [Dataset](#dataset)
- [Model](#model)
- [Performance](#performance)
- [Setup](#setup)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Introduction
This project aims to predict car prices based on various features using a machine learning approach. The Random Forest model was chosen for its effectiveness in handling regression problems and was trained to achieve a reasonable accuracy level.

## Technologies Used
- **Python** for data processing and model building
- **Pandas** for data manipulation
- **Scikit-Learn** for model implementation
- **Matplotlib/Seaborn** for data visualization (if used)

## Dataset
The dataset used for this car price prediction project consists of **19,237 entries** with **18 columns**, capturing various attributes of cars that could influence their market prices. Here is a brief description of each column:

### Features
1. **ID**: Unique identifier for each car record.
2. **Price**: The target variable representing the car's price (in the respective currency).
3. **Levy**: A tax or additional charge, represented as an object (may require preprocessing to convert to a numerical format).
4. **Manufacturer**: The car's make or brand, such as Toyota, BMW, etc.
5. **Model**: Specific model name of the car.
6. **Prod. year**: The year the car was manufactured.
7. **Category**: The type of car (e.g., SUV, sedan, truck, etc.).
8. **Leather interior**: Indicates if the car has a leather interior (usually a binary categorical value like "Yes" or "No").
9. **Fuel type**: The type of fuel the car uses (e.g., Petrol, Diesel, Hybrid, Electric).
10. **Engine volume**: The volume of the engine, which could include extra information (e.g., 2.5L Turbo).
11. **Mileage**: Distance the car has been driven, represented as an object (often in kilometers, requiring conversion to a numerical value).
12. **Cylinders**: Number of cylinders in the car's engine (float type, possibly due to missing values or decimals).
13. **Gear box type**: The type of gearbox (e.g., Automatic, Manual).
14. **Drive wheels**: Indicates the type of drive system (e.g., FWD, RWD, AWD).
15. **Doors**: Number of doors, sometimes represented as an object (e.g., "4", "5+").
16. **Wheel**: The side of the steering wheel (e.g., Left-hand drive or Right-hand drive).
17. **Color**: The exterior color of the car.
18. **Airbags**: Number of airbags in the car.

### Notes
- **Data Preprocessing**: Columns like `Levy`, `Engine volume`, and `Mileage` may require cleaning and conversion to numerical values for modeling purposes. Categorical features such as `Manufacturer`, `Fuel type`, and `Gear box type` might need encoding.
- **Potential Feature Engineering**: Consider extracting additional insights, such as the age of the car from `Prod. year` or binning mileage values into categories.

## Model
- **Algorithm**: Random Forest
- **Metrics**: The model was evaluated using standard regression metrics, achieving an accuracy of **78%**.

### Why Random Forest?
Random Forest is a robust and versatile ensemble learning method that reduces overfitting and improves prediction accuracy by averaging multiple decision trees.

## Performance
The model's performance metrics are as follows:
- **Accuracy**: 78%
- Further evaluation can be done using metrics like RMSE, MAE, etc.

## Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/car-price-prediction.git
