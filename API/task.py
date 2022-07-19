from celery import shared_task
from celery import current_task
import pickle

import pandas as pd
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response


@shared_task()
def MLResualt(self,df):
    try:
        scaler = pickle.load(open(r"Scaler.sav", 'rb'))
        model = pickle.load(open(r"Prediction.sav", 'rb'))
        X = scaler.transform(df)
        y_pred = model.predict(X)
        y_pred = (y_pred > 0.80)
        result = "Yes" if y_pred else "No"
        return result
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)
