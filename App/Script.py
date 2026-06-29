import pandas as pd 
import numpy as np
import streamlit as st
import joblib
# ---------- Page config ----------
st.set_page_config(
    page_title="Titanic Survival Predictor",
    page_icon="🚢",
    layout="centered"
)
@st.cache_resource
def load_model():
    return joblib.load('models/titanic_model.pkl')

model = load_model()

# ---------- Header ----------
st.title("🚢 Titanic Survival Predictor")
st.markdown("""
    Enter a passenger’s details below and find out if they would have survived the Titanic disaster.
    This model was trained on the famous [Kaggle Titanic dataset](https://www.kaggle.com/c/titanic).
""")

st.divider()
with st.form("passenger_form"):
    st.subheader("Passenger Information")

    col1, col2 = st.columns(2)
    with col1:
        pclass = st.selectbox(
            "Ticket Class (1 = 1st, 2 = 2nd, 3 = 3rd)",
            options=[1, 2, 3],
            help="1st class is the most expensive, 3rd is the cheapest. Higher class often had better survival chances."
        )
        sex = st.radio(
            "Sex",
            options=['male', 'female'],
            horizontal=True,
            help="Women and children were given priority on lifeboats."
        )
        age=st.slider("Age(Year)", min_value=1, max_value=80,
                      help="Age of the passenger. Children had higher survival rates.")
    with col2:
        family_size = st.number_input(
            "Family Size (including self)",
            min_value=1, max_value=10, value=1,
            help="Total number of family members aboard (siblings/spouse + parents/children + 1)."
        )
        fare = st.slider(
            "Fare (£)",
            min_value=0.0, max_value=500.0, value=32.0, step=0.5,
            help="Ticket fare in British pounds. Higher fares often meant better cabin locations."
        )
        embarked = st.selectbox(
            "Port of Embarkation",
            options=['S', 'C', 'Q'],
            help="S = Southampton, C = Cherbourg, Q = Queenstown. The port where the passenger boarded."
        )
    submitted = st.form_submit_button("🔮 Predict Survival")
    # ---------- Prediction ----------
if  submitted:
    input_data=pd.DataFrame(
        {'Pclass':[pclass],
        'Sex':[sex],
        'Age':[age],
        'Fare':[fare],
        'Embarked':[embarked],
        'family_size':[family_size]
        })
    with st.spinner("Predicting..."):
        prediction = model.predict(input_data)[0]
    try:
            proba = model.predict_proba(input_data)[0, 1]
            proba_text = f"**Probability of survival:** {proba:.2%}"
    except:
            proba_text = ""
    st.divider()
    st.subheader("Result")
    if prediction == 1:
        st.success(f"✅ The passenger **would survive**.")
    else:
        st.error(f"❌ The passenger **would not survive**.")
    if proba_text:
        st.write(proba_text)
    st.caption("Predictions are based on a machine learning model trained on historical data.")


