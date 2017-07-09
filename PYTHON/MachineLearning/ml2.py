import pandas as pd
import quandl, math, datetime
import numpy as np 
from sklearn import preprocessing,model_selection
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')


""" Getting stock prices data from quandl"""
df = quandl.get("WIKI/GOOGL")

#grabbing useful features
df = df[['Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume']]
#Calculating Percentage change
df['HL_PCT'] = (df['Adj. High'] - df['Adj. Close'])/ df['Adj. Close'] * 100.0
df['PCT_Change'] = (df['Adj. Close'] - df['Adj. Open'])/ df['Adj. Open'] * 100.0

#necessary columns
df = df[['Adj. Close','HL_PCT','PCT_Change','Adj. Volume']]

forecast_col = 'Adj. Close'
#if any data is unavailable,fill it
df.fillna(value=-99999, inplace=True)
#predicting for 1% of data frame 
forecast_out = int(math.ceil(0.01 * len(df)))
print(forecast_out)

""" Shifting the label column i.e Adj. Close column up by forecast_out amount
	It will be our label as they are future prices """
df['label'] = df[forecast_col].shift(-forecast_out)
print (df.head())

#defining features
X = np.array(df.drop(['label'],1))
#defining labels 
y = np.array(df['label'])
#we need to scale X for fast convergence
X = preprocessing.scale(X)

X_lately = X[-forecast_out:]
X = X[:-forecast_out]

df.dropna(inplace = True)
y = np.array(df['label'])

#we ahouls have same length for features and labels
print (len(X), len(y))

#dividing into training and testing sets, test size = 20% of total data
X_train, X_test, y_train, y_test = model_selection.train_test_split(X ,y ,test_size = 0.2)

clf = LinearRegression()
clf.fit(X_train,y_train)
accuracy = clf.score(X_test,y_test)

forecast_set = clf.predict(X_lately)

print(forecast_set, accuracy, forecast_out)

df['Forecast'] = np.nan

last_date = df.iloc[-1].name
last_unix = last_date.timestamp()
one_day = 86400
next_unix = last_unix + one_day