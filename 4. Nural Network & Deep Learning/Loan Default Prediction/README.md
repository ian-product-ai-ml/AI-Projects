# 💸 Lending Club Loan Default Prediction

## 📌 Project Overview
This project builds a deep learning model to predict whether a loan applicant is likely to default, using historical data from Lending Club between 2007 and 2015. Predicting defaults accurately is crucial for lenders to minimize risk and make better credit decisions.

## 🎯 Objective
Train a binary classification model using a neural network to identify potential loan defaults based on borrower and loan attributes.

## 🏦 Domain
Finance / Credit Risk Modeling

---

## 🛠️ Tasks Performed

### 1️⃣ Data Preprocessing
- Encoded categorical variables such as `purpose`.
- Normalized numeric features including income and FICO scores.
- Handled missing values and removed redundant or highly correlated features.

### 2️⃣ Exploratory Data Analysis (EDA)
- Investigated relationships between key features (interest rate, credit score, etc.) and default status.
- Identified severe class imbalance: significantly more non-default (fully paid) loans than defaulted ones.

### 3️⃣ Feature Engineering
- Created a clean set of predictive features, including:
  - `credit.policy`, `int.rate`, `installment`, `log.annual.inc`
  - `dti`, `fico`, `revol.bal`, `revol.util`
  - Credit inquiries, delinquencies, and public records

### 4️⃣ Model Building
- Built a deep learning model using **Keras with TensorFlow backend**.
- Used a feedforward neural network with multiple Dense layers.
- Evaluated model using classification metrics and confusion matrix.

---

## ❗ Key Challenge
Despite decent accuracy, the model struggles with **low recall for default cases**. Due to severe class imbalance, it tends to predict most cases as non-default, missing critical high-risk loans.

---

## ✅ Next Steps

🚀 **Train on a Larger Dataset**  
Expand beyond 2007–2015 to include newer Lending Club records to improve the model’s generalization to current lending patterns.

🚀 **Balance the Classes More Effectively**  
Use techniques like **SMOTE**, **undersampling**, or **class weighting** to boost performance on the minority (default) class.

🚀 **Optimize Model Architecture**  
Test deeper networks, add **Dropout** and **Batch Normalization**, and use **learning rate schedules** to improve training stability and reduce overfitting.

---

## 📂 Dataset Description

| Feature              | Description                                      |
|----------------------|--------------------------------------------------|
| `credit.policy`      | Lending Club's internal credit policy (1 = meets) |
| `purpose`            | Reason for the loan (e.g., credit card, business) |
| `int.rate`           | Interest rate on the loan                        |
| `installment`        | Monthly loan repayment                          |
| `log.annual.inc`     | Log of the borrower's annual income             |
| `dti`                | Debt-to-income ratio                            |
| `fico`               | Credit score                                    |
| `revol.bal`          | Revolving credit balance                        |
| `revol.util`         | Revolving line utilization rate                 |
| `inq.last.6mths`     | Recent credit inquiries                         |
| `delinq.2yrs`        | Number of delinquencies in last 2 years         |
| `pub.rec`            | Number of derogatory public records             |

---

## 📈 Results Summary
The model demonstrates good performance on the majority class but underperforms on identifying actual defaults. This makes class balancing and architectural tuning essential for improvement.