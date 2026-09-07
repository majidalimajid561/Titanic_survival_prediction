from fastapi import FastAPI,HTTPException
from typing import Optional,Annotated,Literal
from pydantic import BaseModel,Field
import joblib
import pandas as pd
from fastapi.responses  import JSONResponse
from schema.user_input import Titanic
from models.predict import survival_prediction,Model_version

app=FastAPI()
@app.get('/')
def home():
    return "This is titanic model APi"
@app.get('/health')
def health_check():
    return {'status':'ok',"version":Model_version,"Model_loaded": Model_version is not None}
@app.post('/predict')
def survival_prediction_(user:Titanic):
    # Because of populate_by_name=True, this function will now run successfully!
    input_data ={
        'Pclass': user.pclass,
        'Sex': user.sex,
        'Age': user.age,
        'Fare': user.fare,
        'Embarked': user.embarked,
        'family_size': user.family_size
        }
    try:
        prediction=survival_prediction(input_data)
        if prediction<1:
           probability=0.4
        else: 
           probability=0.7
        return JSONResponse(status_code=200, content={"prediction": prediction,'probability':probability})
    except Exception as e:
     return JSONResponse(status_code=500,content=str(e))




 
    