import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import mean_squared_error


def sort_dataset(dataset_df):
	#TODO: Implement this function
	df_sorted = dataset_df.sort_values(by='year', ascending=True)
	return df_sorted

def split_dataset(dataset_df):	
	#TODO: Implement this function
	dataset_df['salary'] *= 0.001
	excep_salary = dataset_df.drop(columns=['salary'])
	sal = dataset_df['salary']

	X_train, X_test, Y_train, Y_test = train_test_split(excep_salary, sal, test_size=195, shuffle=False)
	return X_train, X_test, Y_train, Y_test

def extract_numerical_cols(dataset_df):
	#TODO: Implement this function
	numerical_cols = ['age', 'G', 'PA', 'AB', 'R', 'H', '2B', '3B', 'HR', 'RBI', 'SB', 'CS', 'BB', 'HBP', 'SO', 'GDP', 'fly', 'war']
	new_df = dataset_df[numerical_cols]
	return new_df

def train_predict_decision_tree(X_train, Y_train, X_test):
	#TODO: Implement this function
	decision_tree = DecisionTreeRegressor()
	decision_tree.fit(X_train, Y_train)
	df_predictions = decision_tree.predict(X_test)
	return df_predictions


def train_predict_random_forest(X_train, Y_train, X_test):
	#TODO: Implement this function
	random_forest = RandomForestRegressor()
	random_forest.fit(X_train, Y_train)
	rf_predictions = random_forest.predict(X_test)
	return rf_predictions


def train_predict_svm(X_train, Y_train, X_test):
	#TODO: Implement this function
	model_pipeline = Pipeline([
		('scaler', StandardScaler()), ('svm' , SVC())
		])
	model_pipeline.fit(X_train, Y_train)
	svm_predictions = model_pipeline.predict(X_test)
	return svm_predictions


def calculate_RMSE(labels, predictions):
	#TODO: Implement this function
	mse = mean_squared_error(labels, predictions)
	rmse = np.sqrt(mse)
	return rmse


if __name__=='__main__':
	#DO NOT MODIFY THIS FUNCTION UNLESS PATH TO THE CSV MUST BE CHANGED.
	data_df = pd.read_csv('2019_kbo_for_kaggle_v2.csv')
	
	sorted_df = sort_dataset(data_df)	
	X_train, X_test, Y_train, Y_test = split_dataset(sorted_df)
	
	X_train = extract_numerical_cols(X_train)
	X_test = extract_numerical_cols(X_test)

	dt_predictions = train_predict_decision_tree(X_train, Y_train, X_test)
	rf_predictions = train_predict_random_forest(X_train, Y_train, X_test)
	svm_predictions = train_predict_svm(X_train, Y_train, X_test)
	
	print ("Decision Tree Test RMSE: ", calculate_RMSE(Y_test, dt_predictions))	
	print ("Random Forest Test RMSE: ", calculate_RMSE(Y_test, rf_predictions))	
	print ("SVM Test RMSE: ", calculate_RMSE(Y_test, svm_predictions))