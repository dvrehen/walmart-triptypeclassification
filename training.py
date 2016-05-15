import pandas as pd
import numpy as np
from sklearn import cross_validation
import xgboost as xgb
import datetime as dt

pd.set_option('max_rows', 10)

params = {'objective': 'multi:softprob',
          'eval_metric': 'mlogloss',
          'num_class': 38}
num_rounds = 300

print("Train a XGBoost model")
val_size = 100000
#train = train.sort(['Date'])
#X_train, X_test = cross_validation.train_test_split(final_df, test_size=0.01)
#X_train, X_test = train.head(len(train) - val_size), train.tail(val_size)

feature_count = X_train.shape[1]
#feature_count = 80
#train_data = X_train[:,1:feature_count]
#test_data = X_test[:,1:feature_count]
dtrain = xgb.DMatrix(data = X_train[:,2:feature_count], label = X_train[:,0].todense() - 2) #- 1)
dvalid = xgb.DMatrix(data = X_test[:,2:feature_count], label = X_test[:,0].todense() - 2) #- 1)
#dvalid = xgb.DMatrix(X_test[features], np.log(X_test["Sales"] + 1))
#dtest = xgb.DMatrix(test[features])
watchlist = [(dvalid, 'eval'), (dtrain, 'train')]
gbm = xgb.train(params, dtrain, num_rounds, evals=watchlist, early_stopping_rounds=50)

gbm.save_model('model\\base_v2.model')
gbm.dump_model('model\\base_v2.dmp', with_stats=True)
#print("Validating")
#train_probs = gbm.predict(xgb.DMatrix(X_test[features]))
#indices = train_probs < 0
#train_probs[indices] = 0
#error = rmspe(np.exp(train_probs) - 1, X_test['Sales'].values)
#print('error', error)
