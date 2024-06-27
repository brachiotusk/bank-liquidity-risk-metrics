

import numpy as np
import math
import scikit as sk
import matplotlib as plt
import pandas as pd
from pandas_datareader import data as pdr
import fix_yahoo_finance as yf
import numpy as np
import datetime as dt
from scipy.stats import norm

class VaR(object):
    def __init__(self):
        self.ticker = []
        self.weight = np.array([])
    def Stock(Ticker, weight):
        self.ticker += Ticker
        self.weight += weight
    def varOneDay(init, conf):
        initinvest = init
        data = pdr.get_data_yahoo(self.ticker, start="2018-01-01", end=dt.date.today())['Close']
        returns = data.pct_change()
        returns.tail()
        covmatrix = returns.cov()
        avg_rets = returns.mean()
        port_mean = avg_rets.dot(self.weight)
        port_stdev = np.sqrt(weights.T.dot(covmatrix).dot(self.weight))
        mean_inv = (1 + port_mean) * initinvest
        inv_stdev = initinvest * port_stdev
        cutoff = norm.ppf(conf,mean_inv,inv_stdev)
        var_d1 = initinvest - cutoff
        return var_d1
    def VarTime(init,conf,tenor):
        var_time = VaR.varOneDay(init,conf)
        varlong = []
        for x in range(1, tenor+1):    
            varlong.append(np.round(var_1d1 * np.sqrt(x),2))
            print(str(x) + " day VaR @ 95% confidence: " + str(np.round(var_time * np.sqrt(x),2)))
    def PlotVaR(init,conf,tenor):
        plotvar = VaR.VarTime(init,conf,tenor)
        plt.xlabel("Day #")
        plt.ylabel("Max portfolio loss (USD)")
        plt.title("Max portfolio loss (VaR) over 15-day period")
        plt.plot(plotvar, "r")

class HQLA(object):
    def __init__(self):
    #based off credit risk over a certain maturity following https://www.bis.org/publ/bcbs279.pdf
        self.exchanges = ["XNYS", "XNAS", "XAMS", "XBRU", "XMSM", "XLIS", "XMIL", "XOSL", "XPAR", "XSHG", "XJPX", "XSHE", "XBOM", "XNSE", "XHKG", "XTSE", "XLON", "XSAU", "XFRA", "XSWX", "XCSE", "XSTO", "XHEL", "XTAL", "XRIS", "XLIT", "XICE"]
    def risk(credit, tenor):
    def valuation():
    def correlation():
    def transparency(Exc):
        for x in self.exchanges:
            if x == Exc:
                print("Transparent")
    def market():
    def volatility():
    
