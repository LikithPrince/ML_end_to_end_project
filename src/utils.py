import os
import sys
import numpy as np
import pandas as pd
import dill
from src.logger import logging
from src.exception import CustomeException
from sklearn.metrics import r2_score

def save_object(file_path, obj):
   try:
      dir_path = os.path.dirname(file_path)
      os.makedirs(dir_path, exist_ok= True)
      with open(file_path, 'wb') as file_obj:
         dill.dump(obj, file_obj)
         logging.info("Pickel file saved")

   except Exception as e:
      raise CustomeException(e, sys)
   

def evaluate_models(x_train, y_train, x_test, y_test, models):
   try:
      report = {}
      for i in range(len(list(models))):
         model = list(models.values())[i]
         model.fit(x_train,y_train)
         y_train_pred = model.predict(x_train)
         y_test_pred = model.predict(x_test)
         train_model_score = r2_score(y_train, y_train_pred)
         test_model_score = r2_score(y_test, y_test_pred)
         # report[model.name] = {'train_score': train_model_score, 'test_score': test_model_score}
         report[list(models.keys())[i]] = test_model_score

      return report
   except Exception as e:
      raise CustomeException(e, sys)
   
