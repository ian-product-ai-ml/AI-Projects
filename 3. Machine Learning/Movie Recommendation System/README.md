# 🎬 Movie Recommendation System  

## 📌 Project Overview  
This project builds a **Movie Recommendation System** using **User-Based and Item-Based Collaborative Filtering** methods. The system suggests movies to users based on their past interactions and preferences of similar users or similar movies.  

## 🎯 Features  
🔹 **User-Based Collaborative Filtering** – Recommends movies based on similar users’ preferences.  
🔹 **Item-Based Collaborative Filtering** – Suggests movies similar to those a user has already watched and liked.  
🔹 **Similarity Computation** – Uses **cosine similarity** to measure relationships between users and movies.  
🔹 **Movie Ratings Data** – Processes movie ratings to identify preferences.  
🔹 **Scalable Recommendation System** – Can be extended with hybrid filtering or deep learning models.  

## 🛠️ Steps Performed  

### **1️⃣ Data Preprocessing**  
✅ Load and explore the dataset (movies, ratings).  
✅ Handle missing values and format the data for analysis.  
✅ Create a **User-Movie Ratings Matrix** for collaborative filtering.  

### **2️⃣ Similarity Computation**  
✅ Compute **User-User Similarity** using **cosine similarity**.  
✅ Compute **Item-Item Similarity** to find related movies.  

### **3️⃣ Recommendation Models**  
✅ **User-Based Collaborative Filtering**  
   - Find similar users and recommend movies they liked.  
✅ **Item-Based Collaborative Filtering**  
   - Identify movies similar to those a user has rated highly.  

### **4️⃣ Model Evaluation & Results**  
✅ Compare recommendations from both methods.  
✅ Test with sample users to verify recommendation quality.  

## 🔍 Future Enhancements  
🚀 **Hybrid Recommendation System** – Combine user and item-based methods for better accuracy.  
🚀 **Deep Learning Models** – Implement a neural network-based recommender system.  

