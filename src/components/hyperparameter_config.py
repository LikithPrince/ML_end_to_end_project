

params={
               "Decision Tree Regressor": {
                  'criterion':['squared_error', 'friedman_mse', 'absolute_error', 'poisson'],
               },
               
               "Random Forest Regressor":{
                  'n_estimators': [8,16,32,64,128,256]
               },

               "Gradient Boosting":{
                  'learning_rate':[.1,.01,.05,.001],
                  'subsample':[0.6,0.7,0.75,0.8,0.85,0.9],
                  'n_estimators': [8,16,32,64,128,256]
               },

               "Linear Regression":{},
               
               "XGBoost Regressor":{
                  'learning_rate':[.1,.01,.05,.001],
                  'n_estimators': [8,16,32,64,128,256]
               },

               "CatBoost Regressor":{
                  'depth': [6,8,10],
                  'learning_rate': [0.01, 0.05, 0.1],
                  'iterations': [30, 50, 100]
               },

               "AdaBoost Regressor":{
                  'learning_rate':[.1,.01,0.5,.001],
                  'n_estimators': [8,16,32,64,128,256]
               },

               "KNeighbors Regressor" : {}
               
         }