# 🏛️ Preserving Heritage: Enhancing Tourism with AI

## 📌 Project Overview
This project uses AI to support heritage preservation and enhance tourism in Indonesia. It is divided into two parts:

1. **Image Classification of Historical Structures** using CNNs and Transfer Learning.
2. **Tourist Recommendation Engine** using collaborative filtering based on user preferences and ratings.

The work combines computer vision and recommender systems to improve tourism planning, personalized travel, and structure maintenance prediction.

---

## 🧠 Part 1: Image Classification of Heritage Structures

### 🎯 Goal
Build a model that can predict the **category of a historical structure** from an image using **transfer learning**.

### 🛠️ Key Steps
- Used a **pretrained CNN** backbone (e.g., VGG16 or ResNet) with frozen convolutional layers.
- Added custom **dense layers with dropout** for regularization.
- Configured the model with appropriate **loss function, optimizer, and callbacks**.
- Trained the model with and without **image augmentation**.
- Visualized **accuracy and loss curves** to detect overfitting and training performance.

---

## 🧠 Part 2: Tourist Recommendation Engine

### 🎯 Goal
Create a recommendation system to suggest destinations based on user ratings and preferences.

### 🛠️ Data Used
- `user.csv`: User demographics (age, user ID, city)
- `tourism_with_id.csv`: Tourist place details (name, category, city, price, time, coordinates)
- `tourism_rating.csv`: User ratings for various places

### 🔍 Exploratory Data Analysis (EDA)
- Analyzed **age distribution** and **rating patterns** by users.
- Identified most popular categories and cities based on total ratings.
- Cleaned missing values and merged datasets for better insights.

### 💡 Recommendation Model
- Built a **Collaborative Filtering model** using user-item interaction matrix.
- Used `UserId`, `PlaceId`, and `Ratings` to compute similarity.
- Generated personalized recommendations based on current tourist location.

---

## ✅ Next Steps

🚀 Improve the CNN model with **more labeled images** or **fine-tuning** of deeper pretrained layers.  
🚀 Integrate **content-based filtering** to handle cold-start problems in the recommender.  
🚀 Build an interactive tourism platform or **web app** to deploy both models together.

---

## 📁 Download Dataset
Download the training images from [Google Drive](https://drive.google.com/file/d/18URa7yCU2fcTO17duZB_cxT0BmfZjQBZ/view?usp=sharing)


## 🧠 Tech Stack
- Python, TensorFlow, Keras, Pandas, NumPy, Matplotlib, Seaborn  
- OpenCV (for image visualization)  
- Scikit-learn (for evaluation and collaborative filtering support)

---

This project showcases how AI can help **protect heritage**, support **personalized tourism**, and drive **data-driven cultural promotion**.
