'''
Created on Nov 5, 2016

@author: ashutosh
'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

mydata=pd.read_csv("NSE/VARUNSHIP.csv")
prices=np.array(mydata['Close'])

def ema(prices, period, ema_type=2):
    num_prices = len(prices)

    if num_prices < period:
        # show error message
        raise SystemExit('Error: num_prices < period')

    if ema_type == 0:  # 1st value is the average of the period
        ema_range = num_prices - period + 1

        emas = np.zeros(ema_range)

        emas[0] = np.mean(prices[:period])

        w = 2 / float(period + 1)

        # only required for the 4th formula
        #w = 1 - 2 / float(period + 1)

        for idx in range(1, ema_range):
            emas[idx] = w * prices[idx + period - 1] + (1 - w) * emas[idx - 1]

            # or with the 2nd formula
            #emas[idx] = emas[idx - 1] + w * ((prices[idx + period - 1] -
            #                                 emas[idx - 1]))

            # or with the 4th formula
            #emas[idx] = w * emas[idx - 1] + (1 - w) * prices[idx + period - 1]

    elif ema_type == 1:  # 1st value is the 1st price
        ema_range = num_prices

        emas = np.zeros(ema_range)

        emas[0] = prices[0]

        w = 2 / float(period + 1)

        # only required for the 4th formula
        #w = 1 - 2 / float(period + 1)

        for idx in range(1, ema_range):
            emas[idx] = w * prices[idx] + (1 - w) * emas[idx - 1]

            # or with the 2nd formula
            #emas[idx] = emas[idx - 1] + w * (prices[idx] - emas[idx - 1])

            # or with the 4th formula
            #emas[idx] = w * emas[idx - 1] + (1 - w) * prices[idx]

    else:
        ema_range = num_prices - period + 1

        emas = np.zeros(ema_range)

        w = 2 / float(period + 1)

        k = 1 / float(1 - w)

        for idx in range(ema_range):
            for period_num in range(period):
                # this runs the prices backwards to comply with the formula
                emas[idx] += w**period_num * \
                    prices[idx + period - period_num - 1]
            emas[idx] /= k
            #print(emas)

   # print (emas[0:10])
    #print(prices[0:10])
    y=emas
    x=mydata.index.values

    #plt.plot(y)
    #plt.plot(prices)
    #plt.show()
if __name__=="__main__": 
    ema(prices, 20, ema_type=2)
