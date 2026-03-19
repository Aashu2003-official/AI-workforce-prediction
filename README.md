# 📊 Employee Growth Prediction using Machine Learning

## 🚀 Project Overview

This project predicts the **future number of employees in companies** using historical data (2018–2025).
It uses **Machine Learning models** to forecast employee growth for **2026 and beyond**.

The project compares:

* 🌳 **XGBoost Regressor**
* 📈 **Linear Regression**

---

## 📂 Dataset

The dataset contains:

* 🏢 Company names
* 📅 Employee count from **2018 to 2025**
* 📊 Generated realistic data for thousands of companies

Example:

| Company | 2018 | 2019 | ... | 2025 |
| ------- | ---- | ---- | --- | ---- |
| ABC Ltd | 100  | 120  | ... | 400  |

---

## 🧠 Problem Statement

Predict:

* 🔮 Employee count for **2026**
* 🔮 Compare predictions from different ML models

---

## ⚙️ Models Used

### 1️⃣ Linear Regression

* Simple and interpretable model
* Learns linear trends in employee growth

### 2️⃣ XGBoost Regressor

* Advanced ensemble model
* Handles complex patterns and non-linearity
* Provides higher accuracy

---

## 🔄 Methodology

### ✅ Training

Model is trained using:
2018–2024 → Predict 2025

### 🔮 Prediction

Using sliding window approach:

* 2019–2025 → Predict 2026
* 2020–2026 → Predict 2027

---

## 📊 Model Comparison

We compare:

* XGBoost predictions (`Emp(2026)`)
* Linear Regression predictions (`Emp(2026_LR)`)

### Visualizations:

* 📈 Scatter plot (model agreement)
* 📉 Distribution plots
* 📊 Difference histogram

---

## 🛠️ Tech Stack

* Python 🐍
* Pandas
* NumPy
* Scikit-learn
* XGBoost
* Matplotlib / Seaborn

---

## ▶️ How to Run

1. Install dependencies:

```bash
pip install pandas numpy scikit-learn xgboost matplotlib seaborn openpyxl
```

2. Run Jupyter Notebook:

```bash
jupyter lab
```

3. Execute cells to:

* Train models
* Predict 2026
* Export results

---

## 📈 Results

* XGBoost shows better performance on complex trends
* Linear Regression provides baseline comparison
* Forecasting works effectively using time-series approach

---

## 💡 Key Learnings

* Time-series forecasting using sliding window
* Model comparison (Linear vs Boosting)
* Data preprocessing and feature engineering
* Real-world ML pipeline implementation

---

## 🔥 Future Improvements

* Add more features (revenue, industry, etc.)
* Use deep learning (LSTM)
* Build web app using Streamlit
* Deploy model

---

## 👨‍💻 Author

**Aashutosh**
Machine Learning Enthusiast 🚀

---

## ⭐ If you like this project

Give it a ⭐ on GitHub!
<img width="1920" height="1080" alt="Screenshot 2026-03-19 211258" src="https://github.com/user-attachments/assets/a3f910cd-6176-46d2-bcd4-450df5cbee1c" />
<img width="1920" height="1080" alt="Screenshot 2026-03-19 211318" src="https://github.com/user-attachments/assets/6b19867c-<img width="1920" height="1080" alt="Screenshot 2026-03-19 211345" src="https://github.com/user-attachments/assets/b9b12c8c-bd11-4a83-83cf-21d3650f6f30" />
7c94-4997-b000-e29d8507c6e1" />
