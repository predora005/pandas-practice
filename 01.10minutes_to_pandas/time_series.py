# coding: utf-8

import numpy as np
import pandas as pd

##################################################
# メイン
##################################################
if __name__ == '__main__':
    
    print("------------------------------------------------------------------")
    print("Time series")
    print("------------------------------")
    rng = pd.date_range('1/1/2012', periods=100, freq='1S')
    print("rng = pd.date_range('1/1/2012', periods=100, freq='1S')")
    print(rng)
    print("------------------------------")
    ts = pd.Series(np.random.randint(0, 500, len(rng)), index=rng)
    print("ts = pd.Series(np.random.randint(0, 500, len(rng)), index=rng)")
    print(ts)
    print("------------------------------")
    # resampleで1Minごとのグループに集約
    ts2 = ts.resample('1Min').sum()
    print("ts.resample('1Min').sum()")
    print(ts2)
    
    print("------------------------------------------------------------------")
    print("Time zone representation:")
    print("------------------------------")
    rng2 = pd.date_range('3/6/2012 00:00', periods=50, freq='D')
    print("rng2 = pd.date_range('3/6/2012 00:00', periods=50, freq='D')")
    print(rng2)
    print("------------------------------")
    ts2 = pd.Series(np.random.randn(len(rng2)), rng2)
    print("ts2 = pd.Series(np.random.randn(len(rng2)), rng2)")
    print(ts2)
    print("------------------------------")
    ts2_utc = ts.tz_localize('UTC')
    print("ts2_utc = ts.tz_localize('UTC')")
    print(ts2_utc)
    
    print("------------------------------------------------------------------")
    print("Converting to another time zone:")
    print("------------------------------")
    ts2_us = ts.tz_localize('US/Eastern')
    print("ts2_utc = ts.tz_localize('US/Eastern')")
    print(ts2_utc)
    
    
    print("------------------------------------------------------------------")
    print("Converting between time span representations:")
    print("------------------------------")
    rng3 = pd.date_range('1/1/2012', periods=10, freq='M')
    print("rng3 = pd.date_range('1/1/2012', periods=10, freq='M')")
    print(rng3)
    print("------------------------------")
    ts3 = pd.Series(np.random.randn(len(rng3)), index=rng3)
    print("ts3 = pd.Series(np.random.randn(len(rng3)), index=rng3)")
    print(ts3)
    print("------------------------------")
    ps3_period = ts3.to_period('M')
    print("ps3_period = ts3.to_period('M')")
    print(ps3_period)
    print("------------------------------")
    ps3_timestamp = ps3_period.to_timestamp('D', how='start')
    print("ps3_timestamp = ps3_period.to_timestamp('D', how='start')")
    print(ps3_timestamp)
    
    print("------------------------------------------------------------------")
    print("Converting between period and timestamp enables some convenient arithmetic functions to be used. ")
    print("------------------------------")
    #prng = pd.period_range('199001', '199212', freq='M')
    prng = pd.period_range('1990Q1', '1992Q4', freq='Q-NOV')
    print("prng = pd.period_range('1990Q1', '1992Q4', freq='Q-NOV')")
    print(prng)
    print("------------------------------")
    tsp = pd.Series(np.random.rand(len(prng)), prng)
    print("tsp = pd.Series(np.random.rand(len(prng)), prng)")
    print(tsp)
    print("------------------------------")
    tsp.index = prng.asfreq(freq='M', how='end') + 1
    print("tsp.index = prng.asfreq(freq='M', how='end') + 1")
    print(tsp)
    print("------------------------------")
    tsp.index = (prng.asfreq('M','e') + 0).asfreq(freq='H', how='s') + 9
    print("(tsp.index = prng.asfreq('M','e') + 1).asfreq(freq='H', how='s') + 9")
    print(tsp)
    