import pandas as pd
import numpy as np
from sklearn import cross_validation
import xgboost as xgb
import datetime as dt

pd.set_option('max_rows', 10)

# Thanks to Chenglong Chen for providing this in the forum
def ToWeight(y):
    w = np.zeros(y.shape, dtype=float)
    ind = y != 0
    w[ind] = 1./(y[ind]**2)
    return w

def rmspe(yhat, y):
    w = ToWeight(y)
    rmspe = np.sqrt(np.mean( w * (y - yhat)**2 ))
    return rmspe

def rmspe_xg(yhat, y):
    # y = y.values
    y = y.get_label()
    y = np.exp(y) - 1
    yhat = np.exp(yhat) - 1
    w = ToWeight(y)
    rmspe = np.sqrt(np.mean(w * (y - yhat)**2))
    return "rmspe", rmspe

# Dummy coding
def toBinary(featureCol, df):
    values = set(df[featureCol].unique())
    newCol = [featureCol + '_' + val for val in values]
    for val in values:
        df[featureCol + '_' + val] = df[featureCol].map(lambda x: 1 if x == val else 0)
    return newCol