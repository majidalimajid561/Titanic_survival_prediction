# ============================================================
# FILE: app.py
# PURPOSE: Streamlit UI for Titanic Survival Prediction
# LAYOUT: Centered, Compact, No Form
# ============================================================

import streamlit as st
import requests

# ============================================
# 1. PAGE CONFIG
# ============================================
st.set_page_config(
    page_title="Titanic Survival Predictor",
    page_icon="🚢",
    layout="centered"
)

# ============================================
# 2. API ENDPOINT
# ============================================
API_URL = "http://localhost:8000/predict"

# ============================================
# 3. HEADER
# ============================================
st.markdown("""
    <div style="text-align: center; padding: 0.5rem 0 0.5rem 0;">
        <h1 style="font-size: 2.8rem; margin: 0;">🚢 Titanic Survival</h1>
        <p style="color: #5e6f8d; font-size: 1rem; margin: 0;">Enter passenger details to predict survival</p>
    </div>
""", unsafe_allow_html=True)

st.divider()

# ============================================
# 4. INPUT SECTION (No Form)
# ============================================

# --- Row 1: Pclass + Sex ---
col1, col2 = st.columns(2)

with col1:
    pclass = st.selectbox(
        "🎫 Class",
        options=[1, 2, 3],
        format_func=lambda x: {1: "1st Class", 2: "2nd Class", 3: "3rd Class"}[x]
    )

with col2:
    sex = st.radio(
        "⚧️ Sex",
        options=['male', 'female'],
        horizontal=True,
        label_visibility="collapsed" if False else "visible"
    )
    # Re-add label for clarity
    st.caption("⚧️ Sex")  # Small label above radio

# --- Row 2: Age + Family Size ---
col1, col2 = st.columns(2)

with col1:
    age = st.slider(
        "📅 Age",
        min_value=1,
        max_value=80,
        value=30
    )

with col2:
    family_size = st.number_input(
        "👨‍👩‍👧 Family Size",
        min_value=1,
        max_value=10,
        value=1,
        help="Yourself + siblings/spouse + parents/children"
    )

# --- Row 3: Fare + Embarked ---
col1, col2 = st.columns(2)

with col1:
    fare = st.slider(
        "💷 Fare (£)",
        min_value=0.0,
        max_value=500.0,
        value=32.0,
        step=0.5
    )

with col2:
    embarked = st.selectbox(
        "⚓ Embarked",
        options=['S', 'C', 'Q'],
        format_func=lambda x: {"S": "Southampton", "C": "Cherbourg", "Q": "Queenstown"}[x]
    )

# ============================================
# 5. PREDICT BUTTON (Outside Form)
# ============================================
st.divider()

predict_button = st.button(
    "🔮 Predict Survival",
    type="primary",
    use_container_width=True
)

# ============================================
# 6. PREDICTION LOGIC
# ============================================
if predict_button:

    # --- Prepare Payload ---
    payload = {
        "pclass": pclass,
        "sex": sex,
        "age": age,
        "fare": fare,
        "embarked": embarked,
        "family_size": family_size
    }

    # --- Call API ---
    try:
        response = requests.post(API_URL, json=payload, timeout=10)

        if response.status_code == 200:
            result = response.json()

            # Expected: {'prediction': 0 or 1, 'probability': 0.xx}
            prediction = result.get('prediction', 0)
            probability = result.get('probability', 0.5)

            # --- Display Summary ---
            st.divider()
            st.markdown("#### 📊 Passenger Summary")
            
            # Compact summary row
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("Class", f"{pclass}")
            with col2:
                st.metric("Sex", sex.capitalize())
            with col3:
                st.metric("Age", f"{age}")
            with col4:
                st.metric("Family", f"{family_size}")

            col1, col2 = st.columns(2)
            with col1:
                st.metric("Fare", f"£{fare:.2f}")
            with col2:
                port_names = {"S": "Southampton", "C": "Cherbourg", "Q": "Queenstown"}
                st.metric("Embarked", port_names.get(embarked, embarked))

            # --- Display Result ---
            st.divider()
            st.markdown("#### 🏆 Result")

            if prediction == 1:
                st.markdown(f"""
                    <div style="background: #e6f7ee; padding: 1.2rem; border-radius: 12px; text-align: center; border: 2px solid #0b6e4f;">
                        <div style="font-size: 2.5rem;">🎉</div>
                        <div style="font-size: 1.8rem; font-weight: 700; color: #0b6e4f;">SURVIVED</div>
                        <div style="font-size: 0.9rem; color: #5e6f8d;">Confidence: <strong>{probability:.1%}</strong></div>
                    </div>
                """, unsafe_allow_html=True)
                
                # Progress bar
                st.progress(probability, text=f"{probability:.1%} survival probability")
                
                if probability > 0.7:
                    st.balloons()
                    st.success("✨ High confidence — likely survived!")
                else:
                    st.info("📊 Moderate confidence prediction.")

            else:
                st.markdown(f"""
                    <div style="background: #fde8e8; padding: 1.2rem; border-radius: 12px; text-align: center; border: 2px solid #b91c1c;">
                        <div style="font-size: 2.5rem;">💔</div>
                        <div style="font-size: 1.8rem; font-weight: 700; color: #b91c1c;">DID NOT SURVIVE</div>
                        <div style="font-size: 0.9rem; color: #5e6f8d;">Confidence: <strong>{probability:.1%}</strong></div>
                    </div>
                """, unsafe_allow_html=True)
                
                # Progress bar
                st.progress(probability, text=f"{probability:.1%} survival probability")
                
                if probability < 0.3:
                    st.warning("⚠️ Low survival probability — unlikely to survive.")
                else:
                    st.info("📊 Moderate confidence prediction.")

        else:
            try:
                error_detail = response.json()
                st.error(f"❌ API Error: {error_detail.get('detail', response.text)}")
            except:
                st.error(f"❌ API Error (Status {response.status_code})")

    except requests.exceptions.ConnectionError:
        st.error(f"❌ Cannot connect to FastAPI at {API_URL}")
        st.info("💡 Run: `uvicorn main:app --reload`")

    except Exception as e:
        st.error(f"❌ Error: {str(e)}")

# ============================================
# 7. FOOTER
# ============================================
st.divider()
st.markdown("""
    <div style="text-align: center; color: #5e6f8d; font-size: 0.75rem;">
        🚢 Titanic Predictor &bull; Streamlit + FastAPI
    </div>
""", unsafe_allow_html=True)
