import streamlit as st
import joblib
import numpy as np

# Load the trained Lasso model
model = joblib.load('lasso_model.pkl')  # Make sure file name is correct

# Streamlit App Title
st.title("🚗 Car Price Predictor using Lasso Regression")

# User input fields
year = st.number_input("Year of Purchase", min_value=1990, max_value=2025, value=2015)
present_price = st.number_input("Present Price (in Lakhs)", min_value=0.0, value=5.0, step=0.5)
kms_driven = st.number_input("Kilometers Driven", min_value=0, value=30000, step=1000)
fuel_type = st.selectbox("Fuel Type", ["Petrol", "Diesel", "CNG"])
seller_type = st.selectbox("Seller Type", ["Dealer", "Individual"])
transmission = st.selectbox("Transmission Type", ["Manual", "Automatic"])
owner = st.selectbox("Owner Count", [0, 1, 3], index=0)

# Encode categorical values
fuel_type_map = {"Petrol": 0, "Diesel": 1, "CNG": 2}
seller_type_map = {"Dealer": 0, "Individual": 1}
transmission_map = {"Manual": 0, "Automatic": 1}

# Prepare input features as per training order
input_features = np.array([[year,
                            present_price,
                            kms_driven,
                            fuel_type_map[fuel_type],
                            seller_type_map[seller_type],
                            transmission_map[transmission],
                            owner]])

# Predict button
if st.button("Predict Selling Price"):
    predicted_price = model.predict(input_features)
    st.success(f"Estimated Selling Price: ₹ {predicted_price[0]:,.2f} Lakhs")
