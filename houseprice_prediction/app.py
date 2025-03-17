import numpy as np
import joblib
import streamlit as st

# Load trained model
model = joblib.load("house_price_model.pkl")

st.title("🏠 House Price Prediction App")

st.write("Enter the details below to predict the house price:")

# Input fields for all 12 features
bedrooms = st.number_input("Number of Bedrooms", min_value=0, value=3)
bathrooms = st.number_input("Number of Bathrooms", min_value=0, value=2)
sqft_living = st.number_input("Living Area (sqft)", min_value=0, value=1800)
sqft_lot = st.number_input("Lot Size (sqft)", min_value=0, value=5000)
floors = st.number_input("Number of Floors", min_value=0, value=1)
waterfront = st.number_input("Waterfront (0 or 1)", min_value=0, max_value=1, value=0)
view = st.number_input("View Rating (0 to 4)", min_value=0, max_value=4, value=1)
condition = st.number_input("Condition (1 to 5)", min_value=1, max_value=5, value=3)
sqft_above = st.number_input("Above Ground Sqft", min_value=0, value=1500)
sqft_basement = st.number_input("Basement Sqft", min_value=0, value=300)
yr_built = st.number_input("Year Built", min_value=1800, max_value=2025, value=2005)
yr_renovated = st.number_input("Year Renovated (0 if never)", min_value=0, value=0)

# Prepare input for prediction
input_features = np.array([[bedrooms, bathrooms, sqft_living, sqft_lot, floors,
                            waterfront, view, condition, sqft_above, sqft_basement,
                            yr_built, yr_renovated]])

# Predict button
if st.button("Predict Price"):
    prediction = model.predict(input_features)
    st.write(f"🏡 Predicted House Price: **Rs{prediction[0]:,.2f}**")
