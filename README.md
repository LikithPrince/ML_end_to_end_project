# ML_end_to_end_project

## src folder
--> components folder contains,
1. data_ingestion, which collects the data and split the data into Train and Test and save it in artifacts folder.
2. data_transformation, which has a pipeline to transforms/preprocess the numerical data and categorical data and save the preprocessed pkl file in artifacts folder.
3. model_trainer, which contains all the regression models to train and check which is the mest suited model and gives their r-2 score.
4. hyperparameter_config file has the dictionary of all the algorithms with parameters to perform hyperparameter.

--> data_ingestion.py file is the main file for this project.

--> exception.py for exception handling,
--> logger.py for logging the details and,
--> utils.py for some utility functions.

## setup.py
--> setup.py file for packaging.

## app.py
for UI, run app.py from the below command,
python3 app.py

URL : http://127.0.0.1:8000/predictdata

## Deployment
The application is deployed in AWS.