# 📩 Spam Classification with GRU (Gated Recurrent Unit)

## 📌 Project Overview  
This project tackles the problem of SMS spam detection using a **Gated Recurrent Unit (GRU)** model. GRUs are powerful for text classification tasks due to their ability to capture sequential patterns in language. The goal is to classify messages as either **spam** or **ham** (non-spam) based on their content.

## 🎯 Objectives  
- Preprocess and prepare a labeled dataset of SMS messages.  
- Build and train a GRU-based neural network.  
- Evaluate the model's ability to detect spam accurately.  
- Reflect on current limitations and explore future improvements.

## 🛠️ Steps Performed

1. **Data Preprocessing**  
   - Loaded the `SpamCollection.csv` dataset.  
   - Cleaned and tokenized the text.  
   - Padded sequences for equal input length.  
   - Converted spam/ham labels into binary values.

2. **Model Architecture**  
   - Used an **Embedding layer** followed by a **GRU layer** and dense output.  
   - Compiled with **binary cross-entropy loss** and **Adam optimizer**.  
   - Trained the model with validation monitoring.

3. **Results & Evaluation**  
   - While training loss and accuracy looked acceptable, the model **struggled to correctly classify spam messages**.  
   - Most predictions leaned toward "ham", leading to poor recall and F1-score for the spam class.

---

## ❗ Issue Observed  
The model has **high accuracy overall** but **low performance on the minority (spam) class**. This suggests the model is biased toward the more common label — ham — and **failing to catch actual spam messages**, which defeats the purpose of the classifier in practice.

---

## 🔧 Future Improvements

🚀 **Address Class Imbalance**  
   - Use **class weights** or **resampling techniques** (e.g., SMOTE, undersampling ham) to give more importance to spam messages.

🚀 **Improve Input Representations**  
   - Integrate **pretrained embeddings** like GloVe or FastText for richer word understanding.  
   - Consider **subword tokenization** (like Byte Pair Encoding) to reduce OOV (out-of-vocabulary) errors.

🚀 **Enhance Model Capacity**  
   - Stack **multiple GRU layers** or use **Bidirectional GRU** to better capture message context.  
   - Add **Dropout**, **Batch Normalization**, or **Layer Normalization** for better generalization.

🚀 **Refine Evaluation Strategy**  
   - Use metrics like **precision, recall, and F1-score**, especially for the spam class.  
   - Analyze the **confusion matrix** to visualize performance issues.

🚀 **Experiment with Attention**  
   - Add an **attention layer** to help the model focus on key phrases that indicate spam (e.g., "Free", "Click now", "Urgent").

---

## 📂 Dataset Overview  
- **File:** `SpamCollection.csv`  
- **Columns:**  
  - `label`: 'spam' or 'ham'  
  - `message`: SMS message content  
