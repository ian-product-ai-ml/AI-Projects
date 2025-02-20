# 🔍 Fraud Detection ML Model  

## 📌 Project Overview  
This project focuses on **detecting fraudulent financial transactions** using machine learning techniques. The dataset consists of transactional, customer, and merchant information, enabling the identification of fraud patterns. The goal is to develop a **predictive model** that distinguishes between legitimate and fraudulent transactions with high accuracy.  

## 🎯 Features  
🔹 **Data Preprocessing** – Handle missing values, encode categorical features, and normalize numeric variables.  
🔹 **Feature Engineering** – Compute customer age, transaction distance, and other derived features.  
🔹 **Exploratory Data Analysis (EDA)** – Visualize transaction distributions and fraud patterns.  
🔹 **Machine Learning Model Training** – Train ensemble models for fraud detection.  
🔹 **Model Evaluation** – Assess performance using accuracy, precision, recall, and F1-score.  

## 🚀 **Outstanding Model Performance**  
The trained fraud detection model achieves **exceptional accuracy** on both training and test datasets:  

✅ **Train Accuracy:** **100% (1.0)**  
✅ **Test Accuracy:** **96% (0.96)**  

📌 **Classification Report (Train Set)**
- **Precision, Recall, F1-score:** **100% across all fraud and non-fraud transactions.**  
- **Zero misclassifications in the training set.**  

📌 **Classification Report (Test Set)**
- **Precision, Recall, F1-score:** **96% across all fraud and non-fraud transactions.**  
- **High reliability in detecting fraudulent transactions while minimizing false positives.**  

💡 **These results indicate that the model generalizes well while maintaining strong fraud detection capabilities.**  

## 🛠️ Steps Performed  

### **1️⃣ Data Preprocessing**  
✅ **Handle Missing Values** – Apply imputation techniques if required.  
✅ **Encoding** – Convert gender to binary values (Male = 1, Female = 0) and one-hot encode categorical variables.  
✅ **Normalization** – Scale numeric columns such as `amt`, `lat`, `long`, `city_pop`, `merch_lat`, and `merch_long`.  

### **2️⃣ Feature Engineering**  
✅ **Calculate Age** – Derived from transaction date and customer's date of birth.  
✅ **Compute Transaction Distance** – Measure the distance between the customer’s location and the merchant’s location.  

### **3️⃣ Exploratory Data Analysis (EDA)**  
✅ **Analyze Spending Patterns** – Study transaction amount distribution.  
✅ **Visualize Fraud vs. Non-Fraud Transactions** – Identify potential fraud patterns.  
✅ **Plot Geographic Data** – Detect location-based fraud trends.  

### **4️⃣ Model Training**  
✅ **Train-Test Split** – Divide the dataset (e.g., 80-20 split) for model training and evaluation.  
✅ **Ensemble Models** – Use advanced techniques such as **Random Forest, Gradient Boosting, or XGBoost** for fraud detection.  

### **5️⃣ Model Evaluation**  
✅ **Assess Performance** – Measure accuracy, precision, recall, and F1-score to validate model effectiveness.  

## 📂 Dataset Overview  
- **Transaction Details:** Transaction ID, amount, timestamp.  
- **Customer Information:** Credit card number, name, job, and demographics.  
- **Merchant Details:** Merchant name, category, and location.  
- **Location Information:** Customer and merchant coordinates, city, and state.  

## 🔍 Future Enhancements  
🚀 **Deep Learning Models** – Implement neural networks for improved fraud detection.  
🚀 **Real-Time Detection** – Deploy the model using Flask/FastAPI for live fraud monitoring.  
🚀 **Anomaly Detection** – Use unsupervised learning techniques to detect unknown fraud patterns.  
