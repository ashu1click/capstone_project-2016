'''
Created on Nov 3, 2016

@author: divya
'''
import pandas as pd
mydata=pd.read_csv("try.csv")
#mydata=mydata[0:1000]
import matplotlib.dates as mdates
import numpy as np
from numpy import  convolve
import matplotlib.pyplot as plt

def OBV(df, n):  
    i = 0  
    OBV = [0]  
    while i < df.index[-1]:  
        if df.get_value(i + 1, 'Total Trade Quantity') - df.get_value(i, 'Total Trade Quantity') > 0:  
            OBV.append(df.get_value(i + 1, 'Volume'))  
        if df.get_value(i + 1, 'Total Trade Quantity') - df.get_value(i, 'Total Trade Quantity') == 0:  
            OBV.append(0)  
        if df.get_value(i + 1, 'Total Trade Quantity') - df.get_value(i, 'Total Trade Quantity') < 0:  
            OBV.append(-df.get_value(i + 1, 'Volume'))  
        i = i + 1  
    OBV = pd.Series(OBV)  
    OBV_ma = pd.Series(pd.rolling_mean(OBV, n), name = 'OBV_' + str(n))  
    df = df.join(OBV_ma)  
    return df
#two array x and y


x=mydata.index.values
y=mydata['Total Trade Quantity'].values


plt.plot(x,y)
plt.xlabel('Date')
plt.ylabel('Total Trade Quantity')
plt.title('MAX India Limited' )
#plt.legend(['50 days MA', '200 days MA', 'Closing price'], loc='upper left')
plt.show()