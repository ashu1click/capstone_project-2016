'''
Created on Nov 12, 2016

@author: ashutosh
'''
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
import numpy as np
def roc(prices, period=21):
    num_prices = len(prices)

    if num_prices < period:
        # show error message
        raise SystemExit('Error: num_prices < period')

    roc_range = num_prices - period

    rocs = np.zeros(roc_range)

    for idx in range(roc_range):
        rocs[idx] = ((prices[idx + period] - prices[idx]) / prices[idx]) * 100

    return rocs
def rsi(prices, period=14):
    num_prices = len(prices)
    if num_prices < period:
        # show error message
        raise SystemExit('Error: num_prices < period')

    # this could be named gains/losses to save time/memory in the future
    changes = prices[1:] - prices[:-1]
    #num_changes = len(changes)

    rsi_range = num_prices - period

    rsis = np.zeros(rsi_range)

    gains = np.array(changes)
    # assign 0 to all negative values
    masked_gains = gains < 0
    gains[masked_gains] = 0

    losses = np.array(changes)
    # assign 0 to all positive values
    masked_losses = losses > 0
    losses[masked_losses] = 0
    # convert all negatives into positives
    losses *= -1

    avg_gain = np.mean(gains[:period])
    avg_loss = np.mean(losses[:period])

    if avg_loss == 0:
        rsis[0] = 100
    else:
        rs = avg_gain / avg_loss
        rsis[0] = 100 - (100 / (1 + rs))

    for idx in range(1, rsi_range):
        avg_gain = ((avg_gain * (period - 1) + gains[idx + (period - 1)]) /
                    period)
        avg_loss = ((avg_loss * (period - 1) + losses[idx + (period - 1)]) /
                    period)

        if avg_loss == 0:
            rsis[idx] = 100
        else:
            rs = avg_gain / avg_loss
            rsis[idx] = 100 - (100 / (1 + rs))

    return rsis
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
def ema(prices, period, ema_type=0):
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

    return emas
