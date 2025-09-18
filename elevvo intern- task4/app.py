import streamlit as st
import joblib
import numpy as np

# -------------------------------
# Load trained model
# -------------------------------
model = joblib.load("loan_approval_model.pkl")

# -------------------------------
# Streamlit App Layout
# -------------------------------
st.set_page_config(page_title="Loan Approval Prediction", layout="wide")

# Title
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🏦 Loan Approval Prediction App</h1>", unsafe_allow_html=True)
st.write("---")

# Sidebar for Input Features
st.sidebar.header("📋 Enter Applicant Details")

loan_id = st.sidebar.text_input("Loan ID", "L001")
no_of_dependents = st.sidebar.number_input("Number of Dependents", min_value=0, step=1)
education = st.sidebar.selectbox("Education", ["Graduate", "Not Graduate"])
self_employed = st.sidebar.selectbox("Self Employed", ["Yes", "No"])
income_annum = st.sidebar.number_input("Annual Income", min_value=0)
loan_amount = st.sidebar.number_input("Loan Amount", min_value=0)
loan_term = st.sidebar.number_input("Loan Term (months)", min_value=0)
cibil_score = st.sidebar.number_input("CIBIL Score", min_value=300, max_value=900, step=1)
residential_assets_value = st.sidebar.number_input("Residential Assets Value", min_value=0)
commercial_assets_value = st.sidebar.number_input("Commercial Assets Value", min_value=0)
luxury_assets_value = st.sidebar.number_input("Luxury Assets Value", min_value=0)
bank_asset_value = st.sidebar.number_input("Bank Asset Value", min_value=0)

# Main area (Prediction output)
st.subheader("🔮 Prediction Result")

if st.sidebar.button("Predict Loan Status"):
    # Encode categorical features
    education_encoded = 1 if education == "Graduate" else 0
    self_employed_encoded = 1 if self_employed == "Yes" else 0

    # Arrange input data
    input_data = np.array([[
        no_of_dependents,
        education_encoded,
        self_employed_encoded,
        income_annum,
        loan_amount,
        loan_term,
        cibil_score,
        residential_assets_value,
        commercial_assets_value,
        luxury_assets_value,
        bank_asset_value
    ]])

    # Make prediction
    prediction = model.predict(input_data)[0]

    # Show result
    if prediction == 0:
        st.success("🎉 Loan Approved ✅")
    else:
        st.error("🚫 Loan Rejected ❌")

    st.write("---")
    st.markdown("✨ **Note:** Model prediction is based on applicant’s financial and personal details.")
