
params = {'objective': 'multi:softprob',
          'eval_metric': 'mlogloss',
          'max_depth': 10,
          'min_child_weight': 1.15,
          'gamma': 1.15,
          'subsample': 0.90,
          'eta' :0.3,
          'silent':1,
          'num_class': 38}
num_rounds = 3000

#dvalid = xgb.DMatrix(X_test[features], np.log(X_test["Sales"] + 1))
#dtest = xgb.DMatrix(test[features])
watchlist = [(dvalid, 'eval'), (dtrain, 'train')]
gbm = xgb.train(params, dtrain, num_rounds, evals=watchlist, early_stopping_rounds=50)

gbm.save_model('model\\base_v3.model')
gbm.dump_model('model\\base_v3.dmp', with_stats=True)


params = {'objective': 'multi:softprob',
          'eval_metric': 'mlogloss',
          'max_depth': 5,
          'min_child_weight': 1.15,
          'gamma': 1.15,
          'subsample': 0.90,
          'eta' :0.3,
          'silent':1,
          'num_class': 38}
num_rounds = 3000

#dvalid = xgb.DMatrix(X_test[features], np.log(X_test["Sales"] + 1))
#dtest = xgb.DMatrix(test[features])
watchlist = [(dvalid, 'eval'), (dtrain, 'train')]
gbm = xgb.train(params, dtrain, num_rounds, evals=watchlist, early_stopping_rounds=50)

gbm.save_model('model\\base_v6.model')
gbm.dump_model('model\\base_v6.dmp', with_stats=True)




params = {'objective': 'multi:softprob',
          'eval_metric': 'mlogloss',
          'nthread': 4,
          'silent':1,
          'num_class': 38}
num_rounds = 300

#dvalid = xgb.DMatrix(X_test[features], np.log(X_test["Sales"] + 1))
#dtest = xgb.DMatrix(test[features])
watchlist = [(dvalid, 'eval'), (dtrain, 'train')]
gbm = xgb.train(params, dtrain, num_rounds, evals=watchlist, early_stopping_rounds=50)

gbm.save_model('model\\base_v2.model')
gbm.dump_model('model\\base_v2.dmp', with_stats=True)



params = {'objective': 'multi:softprob',
          'eval_metric': 'mlogloss',
          'max_depth': 5,
          'silent':1,
          'num_class': 38}
num_rounds = 3000

#dvalid = xgb.DMatrix(X_test[features], np.log(X_test["Sales"] + 1))
#dtest = xgb.DMatrix(test[features])
watchlist = [(dvalid, 'eval'), (dtrain, 'train')]
gbm = xgb.train(params, dtrain, num_rounds, evals=watchlist, early_stopping_rounds=50)

gbm.save_model('model\\base_v4.model')
gbm.dump_model('model\\base_v4.dmp', with_stats=True)

params = {'objective': 'multi:softprob',
          'eval_metric': 'mlogloss',
          'max_depth': 6,
          'silent':1,
          'num_class': 38}
num_rounds = 3000

#dvalid = xgb.DMatrix(X_test[features], np.log(X_test["Sales"] + 1))
#dtest = xgb.DMatrix(test[features])
watchlist = [(dvalid, 'eval'), (dtrain, 'train')]
gbm = xgb.train(params, dtrain, num_rounds, evals=watchlist, early_stopping_rounds=50)

gbm.save_model('model\\base_v10.model')
gbm.dump_model('model\\base_v10.dmp', with_stats=True)


params = {'objective': 'multi:softprob',
          'eval_metric': 'mlogloss',
          'eta' :0.3,
          'silent':1,
          'num_class': 38}
num_rounds = 3000

#dvalid = xgb.DMatrix(X_test[features], np.log(X_test["Sales"] + 1))
#dtest = xgb.DMatrix(test[features])
watchlist = [(dvalid, 'eval'), (dtrain, 'train')]
gbm = xgb.train(params, dtrain, num_rounds, evals=watchlist, early_stopping_rounds=50)

gbm.save_model('model\\base_v5.model')
gbm.dump_model('model\\base_v5.dmp', with_stats=True)

params = {'objective': 'multi:softprob',
          'eval_metric': 'mlogloss',
          'eta' :0.005,
          'silent':1,
          'num_class': 38}
num_rounds = 3000

#dvalid = xgb.DMatrix(X_test[features], np.log(X_test["Sales"] + 1))
#dtest = xgb.DMatrix(test[features])
watchlist = [(dvalid, 'eval'), (dtrain, 'train')]
gbm = xgb.train(params, dtrain, num_rounds, evals=watchlist, early_stopping_rounds=50)

gbm.save_model('model\\base_v7.model')
gbm.dump_model('model\\base_v7.dmp', with_stats=True)

params = {'objective': 'multi:softprob',
          'eval_metric': 'mlogloss',
          'subsample' : 100,
          'silent':1,
          'num_class': 38}
num_rounds = 3000

#dvalid = xgb.DMatrix(X_test[features], np.log(X_test["Sales"] + 1))
#dtest = xgb.DMatrix(test[features])
watchlist = [(dvalid, 'eval'), (dtrain, 'train')]
gbm = xgb.train(params, dtrain, num_rounds, evals=watchlist, early_stopping_rounds=50)

gbm.save_model('model\\base_v8.model')
gbm.dump_model('model\\base_v8.dmp', with_stats=True)

params = {'objective': 'multi:softprob',
          'eval_metric': 'mlogloss',
          'subsample' :0.90,
          'silent':1,
          'num_class': 38}
num_rounds = 3000

#dvalid = xgb.DMatrix(X_test[features], np.log(X_test["Sales"] + 1))
#dtest = xgb.DMatrix(test[features])
watchlist = [(dvalid, 'eval'), (dtrain, 'train')]
gbm = xgb.train(params, dtrain, num_rounds, evals=watchlist, early_stopping_rounds=50)

gbm.save_model('model\\base_v9.model')
gbm.dump_model('model\\base_v9.dmp', with_stats=True)


