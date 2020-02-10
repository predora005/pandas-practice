# coding: utf-8

import numpy as np
import pandas as pd

##################################################
# メイン
##################################################
if __name__ == '__main__':
    
    dates = pd.date_range('20130101', periods=6)
    df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
    #df['E'] = ['one', 'one', 'two', 'three', 'four', 'three']
    
    print("------------------------------------------------------------------")
    print("Setting a new column automatically aligns the data by the indexes.")
    print("------------------------------")
    s1 = pd.Series(range(1,7), index=pd.date_range('20130102', periods=6))
    print("s1:")
    print(s1)
    print("------------------------------")
    df['F'] = s1
    print("df['F'] = s1")
    print(df)
    
    print("------------------------------------------------------------------")
    print("Setting values by label:")
    print("------------------------------")
    df.at[dates[0], 'A'] = 0
    print("df.at[dates[0], 'A'] = 0")
    print(df)
    print("------------------------------")
    print("Setting values by position:")
    print("------------------------------")
    df.iat[0, 1] = 0
    print("df.iat[0, 1] = 0")
    print(df)
    print("------------------------------")
    print("Setting by assigning with a NumPy array:")
    print("------------------------------")
    df.loc[:, 'D'] = np.array([5] * len(df))
    print("df.loc[:, 'D'] = np.array([5] * len(df))")
    print(df)
    print("------------------------------")
    print("A where operation with setting.")
    print("------------------------------")
    df2 = df.copy()
    index = df2 > 0
    print("df2 > 0")
    print(index)
    print("------------------------------")
    df2[df2 > 0] = -df2
    print("df2[df2 > 0] = -df2")
    print(df2)
