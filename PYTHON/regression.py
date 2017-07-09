# our data is a continous one and
# we try to find a line to best fit them.

import pandas as pd
import Quandl 
import math
import numpy as np 
from sklearn import preprocessing, cross_validation, svm
from sklearn.linear_model import LinearRegression

#getting our data of stock prices
df = Quandl.get('WIKI/GOOGL')

df = df[['Adj.Open','Adj.High','Adj.Low','Adj.Close','Adj.Volume']]
df['HL_PCT'] = (df['Adj.High']) - (df['Ajd.Close'])/ (df['Ajd.Close']) *100.0
df['PCT_CHANGE'] = (df['Adj.Close']) - (df['Adj.Open'])/df['Adj.Open'] * 100.0

#cpdating the data frame with required columns
#these are our features
df = df[['Adj.Close','HL_PCT','PCT_CHANGE','Adj.Volume']]

#printing starting five rows
print(df.head())

forecast_col = 'Adj.Close'
df.fillna(-99999, inplace = True)

forecast_out = int(math.ceil(0.01*len(df)))

#labels are future prices , we are just shifting the Close column upward for label col
df['label'] = df[forecast_col].shift(-forecast_out)
df.dropna(inplace = True)
print(df.head())

#X = features and y = labels
X = np.array(df.drop(['label'],1))
y = np.array(df.['label'])

X = preprocessing.scale(X)

df.dropna(inplace = True)
y = np.array(df.['label'])

X_train,X_test,y_train,y_test = cross_validation.train_test_split(X,y, test_size =0.2)

clf = LinearRegression()
clf.fit(X_train.y_train)
accuracy = clf.score(X_test,y_test)

print(accuracy)







