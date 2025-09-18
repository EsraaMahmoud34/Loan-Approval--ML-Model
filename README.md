# Loan Approval Prediction
## 📌 Project Overview
This project focuses on predicting **loan approval status** using machine learning techniques. The dataset contains various applicant details (income, education, credit history, loan amount, etc.), and the task is to classify whether a loan should be approved or not.  

The workflow includes **exploration, preprocessing, model training, evaluation, and deployment** using Streamlit.

## 📂 Repository Structure

TASK4/
│── app.py                     # Streamlit app for prediction
│── loan\_approval\_dataset.csv  # Dataset used for training
│── loan\_approval\_model.pkl    # Trained Decision Tree model (saved with joblib)
│── loan\_approval.ipynb        # Jupyter notebook (EDA, preprocessing, training, evaluation)
|── requirements.txt


## 🔎 Steps Followed

### 1. Data Exploration & EDA
- Checked dataset structure, missing values, and distributions.  
- Visualized categorical and numerical features.  
- Identified relationships between variables and loan approval.  

### 2. Data Preprocessing
- **Label Encoding** applied on categorical variables.  
- **Scaling** performed on numerical variables for balanced model performance.  
- Train-test split applied (80%-20%).  

### 3. Model Training
Trained multiple models using **GridSearchCV** to tune hyperparameters:
- Logistic Regression  
- Decision Tree   
- XGBoost  
- Support Vector Machine (SVM)  

### 4. Model Evaluation
- Evaluation metrics: **Accuracy, Precision, Recall, F1-score**  
- Best performing model: **Decision Tree Classifier**  
  - Accuracy: **98%**  
  - Precision: **98%**  
  - Recall: **99%**  
  - F1 Score: **99%**

📊 **Confusion Matrix:**  
(Add your confusion matrix image here)  
```

![Confusion Matrix](<img width="519" height="413" alt="image" src="https://github.com/user-attachments/assets/1d93ee28-63c6-42ce-b0a9-0dba31ebdafd" />
)

## 🚀 How to Run

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/loan-approval-prediction.git
cd loan-approval-prediction
````

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit App

```bash
streamlit run app.py
```

---

## 📈 Key Learnings

* Learned the importance of **EDA** in identifying useful patterns before modeling.
* Gained experience with **feature encoding and scaling** to prepare structured data.
* Compared multiple ML algorithms and saw how **Decision Trees** can achieve very high accuracy for structured datasets.
* Learned how to **save models with joblib** and deploy them using **Streamlit** for interactive predictions.

---

## 👩‍💻 Author

**Esraa Mahmoud**
Third-year AI student at Ain Shams University | USAID Scholar Alumni | Passionate about Machine Learning & AI Applications


