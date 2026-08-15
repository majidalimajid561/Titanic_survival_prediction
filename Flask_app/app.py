from flask import Flask, render_template, request
import joblib
import os
import pandas as pd



# MODEL_PATH = os.path.join('models', 'titanic_model.pkl')

try:
    with open("models/titanic_model.pkl", 'rb') as f:
        model = joblib.load(f)
    print("✅ Titanic model loaded successfully!")
except FileNotFoundError:
    print(f"❌ ERROR: Model not found at /models/titanic_model.pkl")
    model = None
app=Flask(__name__)

# You need at least one route to handle browser requests
@app.route('/')
def home():
    return render_template('home.html')
@app.route('/predict',methods=['POST'])
def predict():
    if model is None:
        return render_template(
            'result.html', 
            error="Model not loaded. Please check the 'models' folder.", 
            survived=None,
            probability=None
        )
    try:
        # --- 3b. Get data from the form ---
        # 🔥 FIXED: 'Embarked' (you had a typo 'Embaraked')
        pclass = request.form.get('Pclass')
        sex = request.form.get('Sex')
        age = request.form.get('Age')
        fare = request.form.get('Fare')
        family_size = request.form.get('family_size')
        embarked = request.form.get('Embarked')
        
        # --- 3c. Validate: Check if any field is empty ---
        if not all([pclass, sex, age, fare, family_size, embarked]):
            return render_template(
                'result.html',
                error="All fields are required. Please go back and fill everything.",
                survived=None,
                probability=None
            )
        try:
            pclass = int(pclass)
            age = float(age)
            fare = float(fare)
            family_size = int(family_size)
        except ValueError:
            return render_template(
                'result.html',
                error="Please enter valid numbers for Pclass, Age, Fare, and Family Size.",
                survived=None,
                probability=None
            )
         # --- 3e. Validate ranges ---
        if pclass not in [1, 2, 3]:
            return render_template('result.html', error="Pclass must be 1, 2, or 3.", survived=None, probability=None)
        if age < 0.5 or age > 100:
            return render_template('result.html', error="Age must be between 0.5 and 100.", survived=None, probability=None)
        if fare < 0:
            return render_template('result.html', error="Fare cannot be negative.", survived=None, probability=None)
        if family_size < 0 or family_size > 10:
            return render_template('result.html', error="Family size must be between 0 and 10.", survived=None, probability=None)
        if sex not in ['male', 'female']:
            return render_template('result.html', error="Sex must be 'male' or 'female'.", survived=None, probability=None)
        if embarked not in ['C', 'Q', 'S']:
            return render_template('result.html', error="Embarked must be 'C', 'Q', or 'S'.", survived=None, probability=None)

         # --- 3f. Create DataFrame for the model ---
        # IMPORTANT: The column order MUST MATCH your training data.
        # If you trained with raw columns: ['Pclass', 'Sex', 'Age', 'Fare', 'Embarked', 'family_size']
        input_data = pd.DataFrame([[
            pclass,
            sex,
            age,
            fare,
            embarked,
            family_size
        ]], columns=['Pclass', 'Sex', 'Age', 'Fare', 'Embarked', 'family_size'])
        try:
            # Get probability of survival (class 1)
            probability = model.predict_proba(input_data)[0][1]
            prediction = model.predict(input_data)[0]  # 0 or 1
        except AttributeError:
            # Some models don't have predict_proba (e.g., SVM without probability)
            prediction = model.predict(input_data)[0]
            probability = 1.0 if prediction == 1 else 0.0
        return render_template(
            'result.html',
            survived=int(prediction),
            probability=round(float(probability), 4),
            error=None
        )
    except Exception as e:
        return render_template(
            'result.html',
            error=f"An unexpected error occurred: {str(e)}",
            survived=None,
            probability=None
        )
    

# Fixed the string name and added .run()
if __name__ == '__main__':
    app.run(debug=True)