# -*- coding: utf-8 -*-
"""
Data Preprocessing

Created on Sun Mar 19 10:39:38 2017

@author: Hemanth
"""

# Importing Libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing Datasets
dataset = pd.read_csv('Data.csv')
X = dataset.iloc[:, :-1].values
Y = dataset.iloc[:, -1].values

# Taking care of Missing data
from sklearn.preprocessing import Imputer
imp = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0)
imp = imp.fit(X[:, 1:3])
X[:, 1:3] = imp.transform(X[:, 1:3])

# Encoding Categorical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
le_x = LabelEncoder()
X[:, 0] = le_x.fit_transform(X[:, 0])
ohc = OneHotEncoder(categorical_features = [0])
X = ohc.fit_transform(X).toarray()
le_y = LabelEncoder()
Y = le_y.fit_transform(Y)

# Splitting the dataset into Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.4, random_state = 0)

# Feature scaling for making attribute values fall in to certain range
from sklearn.preprocessing import StandardScaler
sc_x = StandardScaler()
X_train = sc_x.fit_transform(X_train)
X_test = sc_x.transform(X_test)