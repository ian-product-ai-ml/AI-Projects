# 🌳 Decision Tree Practice - Classification & Regression  

## 📌 Project Overview  
This project explores **Decision Tree models** for both **classification and regression** tasks using the **Iris dataset** and a **housing price dataset**. The goal is to understand how decision trees work, how to visualize them, and how to prevent overfitting using **pruning techniques**.  

## 🎯 Features  
🔹 **Classification** – Train a **Decision Tree Classifier** on the Iris dataset.  
🔹 **Regression** – Implement a **Decision Tree Regressor** on housing price data.  
🔹 **Visualization** – Plot decision trees to understand model splits.  
🔹 **Pruning & Hyperparameter Tuning** – Apply techniques like `max_depth`, `min_samples_split`, and **cost-complexity pruning** (`ccp_alpha`).  

## 🛠️ Steps Performed  

### **1️⃣ Decision Tree Classifier (Iris Dataset)**  
✅ **Load and preprocess the dataset**  
✅ **Train-test split** to prepare data for modeling  
✅ **Train a Decision Tree Classifier** and evaluate accuracy  
✅ **Plot the decision tree** for interpretability  

### **2️⃣ Pruning Techniques to Avoid Overfitting**  
✅ **Method 1** – Limit tree depth (`max_depth=3`)  
✅ **Method 2** – Set minimum samples per split (`min_samples_split=10`)  
✅ **Method 3** – Set minimum samples per leaf (`min_samples_leaf=10`)  
✅ **Method 4** – Use cost-complexity pruning (`ccp_alpha=0.001`)  

### **3️⃣ Decision Tree Regressor (Housing Prices-Additional Practice)**  
✅ **Load housing dataset (`house.csv`)**  
✅ **Train a Decision Tree Regressor to predict home prices**  
✅ **Evaluate model performance (train & test scores)**  
✅ **Visualize the regression tree**  

## 📂 Datasets Used  
- **iris.csv** – Features: Sepal length, sepal width, petal length, petal width, and species.  
- **house.csv** – Features: Square footage, number of bedrooms, and price.  

## 🔍 Future Enhancements  
🚀 **Compare Decision Trees with Random Forests & Gradient Boosting**  
🚀 **Optimize hyperparameters using GridSearchCV**  
🚀 **Deploy as a web-based interactive tool**  