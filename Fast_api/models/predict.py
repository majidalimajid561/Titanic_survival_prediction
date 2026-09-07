import joblib
import pandas as pd 
model=None
try:
    with open('../models/titanic_model.pkl','rb') as  f:
       model=joblib.load(f)
       print("model load")
       Model_version='1.0.0'
except:
    raise "model dose not load"
def survival_prediction(user_input):
    if model==None:
        return "model did loaded"
    try:
        input_data=pd.DataFrame([user_input])
        prediction = model.predict(input_data)[0].item()
        return prediction
    except:
        return "there is some error while prediction"


