# 🎵 Spotify Song Cohort Analysis  

## 📌 Project Overview  
This project aims to group songs into **cohorts** based on their characteristics using **clustering techniques**. By analyzing **Rolling Stones' albums on Spotify**, we identify patterns in song attributes and create meaningful song clusters that enhance music recommendations.  

## 🎯 Features  
🔹 **Data Preprocessing** – Clean, transform, and refine Spotify song data.  
🔹 **Exploratory Data Analysis (EDA)** – Visualize key song attributes to detect trends.  
🔹 **Feature Engineering** – Create new insights from audio features.  
🔹 **Popularity Analysis** – Identify the most popular albums and tracks.  
🔹 **Dimensionality Reduction** – Optimize feature space for better clustering.  
🔹 **Cluster Analysis** – Group similar songs using machine learning techniques.  

## 🛠️ Steps Performed  

### **1️⃣ Data Preprocessing**  
✅ Inspect for **duplicates, missing values, and outliers**.  
✅ Standardize and **normalize numerical features** (e.g., loudness, tempo, valence).  

### **2️⃣ Exploratory Data Analysis (EDA)**  
✅ **Visualize feature distributions** (e.g., danceability, energy, speechiness).  
✅ **Analyze song popularity** across albums.  
✅ **Identify the top two recommended albums** based on song popularity.  
✅ **Study relationships** between song features and popularity.  

### **3️⃣ Dimensionality Reduction**  
✅ Use **Principal Component Analysis (PCA)** or other methods to optimize clustering features.  

### **4️⃣ Clustering & Cohort Creation**  
✅ **Determine the optimal number of clusters**.  
✅ Apply **clustering algorithms** (e.g., K-Means, Hierarchical Clustering) to group songs.  
✅ Define clusters based on key song characteristics.  

## 📂 Dataset Overview  
- **name** – Song title  
- **album** – Album name  
- **popularity** – Popularity score (0-100)  
- **acousticness, danceability, energy, loudness, valence** – Audio features  
- **speechiness, tempo, duration_ms** – Additional song characteristics  

## 🔍 Future Enhancements  
🚀 **Hybrid Clustering Approach** – Combine different clustering methods for better accuracy.  
🚀 **Predictive Modeling** – Train a model to recommend songs based on user preferences.  
🚀 **Web App Integration** – Deploy a song recommender as an interactive web application.  