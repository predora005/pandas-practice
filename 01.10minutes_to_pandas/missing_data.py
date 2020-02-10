# coding: utf-8

import numpy as np
import pandas as pd

##################################################
# メイン
##################################################
if __name__ == '__main__':
    
    dates = pd.date_range('20130101', periods=6)
    df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
    s1 = pd.Series(range(1,7), index=pd.date_range('20130102', periods=6))
    df['F'] = s1
    df.at[dates[0], 'A'] = 0
    df.iat[0, 1] = 0
    df.loc[:, 'D'] = np.array([5] * len(df))
    print("------------------------------")
    print("df:")
    print(df)
    
    print("------------------------------------------------------------------")
    print("Reindexing allows you to change/add/delete the index on a specified axis. This returns a copy of the data.")
    print("------------------------------")
    df1 = df.reindex(index=dates[0:4], columns=list(df.columns) + ['E'])
    print("df.reindex(index=dates[0:4], columns=list(df.columns) + ['E'])")
    print(df1)
    print("------------------------------")
    df1.loc[dates[0]:dates[1], 'E'] = 1
    #df1.loc[0:1, 5] = 1
    print("df1.loc[dates[0]:dates[1], 'E'] = 1")
    print(df1)
    
    print("------------------------------------------------------------------")
    print("To drop any rows that have missing data.")
    print("------------------------------")
    df2 = df1.dropna(how='any')
    print("df1.dropna(how='any')")
    print(df2)
    
    print("------------------------------------------------------------------")
    print("Filling missing data.")
    print("------------------------------")
    df2 = df1.fillna(value=99)
    print("df1.fillna(value=99)")
    print(df2)
    
    print("------------------------------------------------------------------")
    print("To get the boolean mask where values are nan.")
    print("------------------------------")
    isna = pd.isna(df1)
    print("pd.isna(df1)")
    print(isna)