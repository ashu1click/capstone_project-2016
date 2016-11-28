'''
Created on Nov 4, 2016

@author: ashutosh
'''

import pandas as pd
mydata=pd.read_csv("NSE/VARUNSHIP.csv")
#mydata=mydata[0:1000]
import matplotlib.dates as mdates
import numpy as np
from numpy import  convolve
import matplotlib.pyplot as plt

def movingaverage(values,window):
    weights=np.repeat(1.0,window)/window
    sma=np.convolve(values,weights,'valid')
    return sma
#two array x and y


x=mydata.index.values
y=mydata['Close'].values
#3 moving average
yMA1=movingaverage(y,50)
yMA2=movingaverage(y, 200)
plt.plot(x[len(x)-len(yMA1):],yMA1)
plt.plot(x[len(x)-len(yMA2):],yMA2)

plt.plot(x,y)
plt.xlabel('Date')
plt.ylabel('Closing price')
plt.title('Varun Shipping Company Limited' )
plt.legend(['50 days MA', '200 days MA', 'Closing price'], loc='upper left')
plt.show()
