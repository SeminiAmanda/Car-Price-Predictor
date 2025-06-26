

# 🚗 Car Price Predictor

A web application to **predict the selling price of used cars** based on various features like model year, kilometers driven, fuel type, etc. This project uses **Linear Regression** and **Lasso Regression** models to provide accurate price predictions.

## 🧠 Models Used

* **Linear Regression**: Captures the overall trend and provides a baseline model.
* **Lasso Regression**: Helps in feature selection by penalizing less important features, preventing overfitting.

## 💡 Features

* Cleaned and preprocessed car dataset
* Feature engineering (Fuel Type, Seller Type, Transmission)
* Model comparison: Linear vs Lasso
* Interactive **Streamlit** UI for prediction
* Real-time price prediction with instant output

## 🌐 App Preview

![Streamlit App Screenshot](./streamlit.png) 

## 🛠️ Tech Stack

* Python
* Pandas, NumPy, Scikit-learn
* Streamlit
* Matplotlib/Seaborn (for visualization)

## 🚀 How to Run Locally

```bash
git clone https://github.com/your-username/car-price-predictor.git
cd car-price-predictor
pip install -r requirements.txt
streamlit run app.py
```

## 📁 Repository Structure

```
├── app.py                # Streamlit app
├── model_linear.pkl      # Trained Linear model
├── model_lasso.pkl       # Trained Lasso model
├── requirements.txt
├── streamlit.png         # App screenshot
└── README.md
```

## 🎯 Sample Prediction Inputs

* Year: 2015
* KM Driven: 55,000
* Fuel Type: Petrol
* Seller Type: Individual
* Transmission: Manual

## 📌 Future Improvements

* Add Random Forest or XGBoost for comparison
* Deploy app on Hugging Face or Render
* Enhance UI/UX with images and graphs

## 📸 App Screenshot

<img src="./streamlit.png" width="800px">

---

