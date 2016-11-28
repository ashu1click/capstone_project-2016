'''
Created on Oct 29, 2016

@author: ashutosh
'''
#code to download the data from quandl using stock's code
import quandl
import pandas as pd
quandl.ApiConfig.api_key='ntJrkqfScL2Ac9PCD4oG'

def download():
    stock_code=pd.read_csv("NSE_STOCK_CODE.csv")
    a=stock_code['Code']
    symbols=a.values.T.tolist()
    
        
    for symbol in symbols:
        mydata=quandl.get("{}".format(symbol))
        mydata.to_csv('{}.csv'.format(symbol))
if __name__=="__main__": 
    download()