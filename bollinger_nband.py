'''
Created on Nov 27, 2016

@author: ashutosh

'''
import numpy as np
import pandas as pd
mydata=pd.read_csv("NSE/VARUNSHIP.csv")
prices=np.array(mydata['Close'])
def sma(prices, period):
    num_prices = len(prices)

    if num_prices < period:
        # show error message
        raise SystemExit('Error: num_prices < period')

    sma_range = num_prices - period + 1

    smas = np.zeros(sma_range)

    # only required for the commented code below
    #k = period

    for idx in range(sma_range):
        # this is the code, but using np.mean below is faster and simpler
        #for period_num in range(period):
        #    smas[idx] += prices[idx + period_num]
        #smas[idx] /= k

        smas[idx] = np.mean(prices[idx:idx + period])

    return smas

def bb(prices, period, num_std_dev=2.0):
    
    num_prices = len(prices)

    if num_prices < period:
        # show error message
        raise SystemExit('Error: num_prices < period')

    bb_range = num_prices - period + 1

    # 3 bands, bandwidth, range and %B
    bbs = np.zeros((bb_range, 6))

    simple_ma = sma(prices, period)

    for idx in range(bb_range):
        std_dev = np.std(prices[idx:idx + period])

        # upper, middle, lower bands, bandwidth, range and %B
        bbs[idx, 0] = simple_ma[idx] + std_dev * num_std_dev
        bbs[idx, 1] = simple_ma[idx]
        bbs[idx, 2] = simple_ma[idx] - std_dev * num_std_dev
        bbs[idx, 3] = (bbs[idx, 0] - bbs[idx, 2]) / bbs[idx, 1]
        bbs[idx, 4] = bbs[idx, 0] - bbs[idx, 2]
        bbs[idx, 5] = (prices[idx] - bbs[idx, 2]) / bbs[idx, 4]

    return bbs
if __name__=="__main__": 
    bb(prices, 20, num_std_dev=2.0)
