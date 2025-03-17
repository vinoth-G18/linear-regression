# House Price Prediction Using Linear Regression

## Introduction
This project aims to predict house prices based on various features using a Linear Regression model. The model is trained on a dataset that includes attributes such as area, number of bedrooms, location, etc. By leveraging linear regression, we aim to establish a relationship between these features and the house prices.

## Dataset
The dataset used for this project contains the following features:
- **Area (in sqft)
- **Number of bedrooms
- **Location
- **Year built
- **Price (target variable) ect...

### Source
The dataset can be obtained from publicly available sources like Kaggle or UCI Machine Learning Repository.

## Requirements
Ensure you have the following dependencies installed:
- Python 3.x
- NumPy
- Pandas
- Scikit-learn
- Matplotlib
- Seaborn

Install dependencies using:
```bash
pip install numpy pandas scikit-learn matplotlib seaborn
```

## Project Structure
```
├── data
│   └── house_prices.csv
├── notebooks
│   └── House_Price_Prediction.ipynb
├── model
│   └── linear_regression_model.pkl
├── app.py (optional for deployment)
├── README.md
```

## Implementation
1. **Data Preprocessing**  
   - Load the dataset
   - Handle missing values
   - Feature scaling for improved model performance

2. **Model Training**  
   - Split data into training and testing sets
   - Train a Linear Regression model
   - Evaluate model performance using metrics like Mean Squared Error (MSE) and R-squared (R²)

3. **Visualization**  
   - Use scatter plots and regression lines to visualize data trends

4. **Deployment (Optional)**  
   - A Streamlit web app can be created for user interaction with the model


## Results
- Achieved **R² score**: ~0.85
- Mean Squared Error (MSE): Lower values indicate better performance

## Deployment
To run the project with a simple UI using **Streamlit**:
```bash
streamlit run app.py
```



