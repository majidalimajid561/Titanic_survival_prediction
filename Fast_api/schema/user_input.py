from fastapi import FastAPI,HTTPException
from typing import Optional,Annotated,Literal
from pydantic import BaseModel,Field


class Titanic(BaseModel):
    # Add this configuration line for Pydantic v2
    pclass:Annotated[Literal[1, 2, 3],Field(...,description="The class were users get seetis and 1 class is higher")]

    sex:Annotated[Literal['male', 'female'],Field(...,description="gender of passenager")]

    age:Annotated[int, Field(...,gt=0,lt=80)]

    family_size:Annotated[int, Field(...,gt=0,lt=10)]

    fare:Annotated[float, Field(...,gt=0,lt=500)]
    
    embarked:Annotated[Literal['S','C','Q'], Field(..., description="From which city did the passengers board?")]
