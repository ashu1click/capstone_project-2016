'''
Created on Nov 4, 2016

@author: ashutosh
'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

mydata=pd.read_csv("NSE/VARUNSHIP.csv")
prices=np.array(mydata['Close'].values)

def roc(prices, period=21):
    num_prices = len(prices)

    if num_prices < period:
        # show error message
        raise SystemExit('Error: num_prices < period')

    roc_range = num_prices - period

    rocs = np.zeros(roc_range)

    for idx in range(roc_range):
        rocs[idx] = ((prices[idx + period] - prices[idx]) / prices[idx]) * 100
        
    y=np.array(rocs).tolist()
    
    print(y[1:10])
    print(np.shape(y))
    x=np.array(mydata.index.values).tolist()
    
    print(x[1:10])
    print(np.shape(x))

    plt.plot(y)
    plt.xlabel('Date')
    plt.ylabel('Closing price')
    plt.legend(['ROC (Rate of change)'], loc='upper left')

    plt.title('Varun Shipping Company Limited' )
    
    
    plt.show()
if __name__=="__main__": 
    roc(prices,period=21)