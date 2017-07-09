import pandas as pd 
import datetime
import matplotlib.pyplot as plt 
from matplotlib import style
import pylab 
import pandas_datareader.data as web
style.use('ggplot')

start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2015, 8, 22)

df = web.DataReader("XOM", 'google', start, end)
print(df.head())



df['High'].plot()
pylab.ion()

