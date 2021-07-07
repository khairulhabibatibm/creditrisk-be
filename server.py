from json_req import Input
import numpy as np
from sklearn.pipeline import make_pipeline
from sklearn.pipeline import make_union
from xgboost import XGBClassifier
import pickle
from fastapi import FastAPI, status, Response
from fastapi.responses import JSONResponse
import requests
import os
from typing import Dict, Any
import pandas as pd


ENV_LOCAL = 'local'
ENV_LIVE = 'live'

CACHE: Dict[str, Any] = {}

# enable documentation for specific environment only
docs_url = '/docs' if os.getenv('ENV') == ENV_LOCAL else None
app = FastAPI(docs_url=docs_url)
modelURL = os.getenv('MODEL_URL')
modelName = 'loaded_model.pkl'

def convert_item_to_df(item: Input) -> pd.DataFrame:
    """Convert Item to the pandas DataFrame"""
    items = {}
    for key, value in item.dict().items():
        items[key] = [value]

    return pd.DataFrame(items)

@app.post('/predict')
async def predict(input:Input,response: Response):
    try:
        loaded_model = pickle.load(open(modelName,'rb'))
    except Exception:
        print('model not found, downloading model')
        # url = "https://ds-public-bucket.s3.jp-tok.cloud-object-storage.appdomain.cloud/new_model.pkl"
        req = requests.get(modelURL,allow_redirects=True)
        open(modelName,'wb').write(req.content)
        loaded_model = pickle.load(open(modelName,'rb'))

    print(input)
    df_input = convert_item_to_df(input)
    print(df_input.iloc[:,0:].values)
    
    prediction = loaded_model.predict(df_input.iloc[:,0:].values)
    print(prediction)

    prediction2 = loaded_model.predict_proba(df_input.iloc[:,0:].values)
    print(prediction2)
    
    return JSONResponse(content={'prediction':prediction[0],'score':str(prediction2[0][0])})