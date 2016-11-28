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

def CCI(df, n):  
    PP = (df['High'] + df['Low'] + df['Close']) / 3  
    CCI = pd.Series((PP - pd.rolling_mean(PP, n)) / pd.rolling_std(PP, n), name = 'CCI_' + str(n))  
    df = df.join(CCI)  
    return df
#two array x and y


x=mydata.index.values
y=mydata['Close'].values
#3 moving average


plt.plot(x,y)
plt.xlabel('Date')
plt.ylabel('Closing price')
plt.title('MAX India Limited' )

plt.show()