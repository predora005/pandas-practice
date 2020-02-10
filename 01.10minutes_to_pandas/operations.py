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
    print("------------------------------------------------------------------")
    print("df:")
    print(df)

    print("------------------------------------------------------------------")
    print("Performing a descriptive statistic:")
    print("------------------------------")
    print("df.mean()")
    print(df.mean())
    print("------------------------------")
    print("Same operation on the other axis:")
    print("------------------------------")
    print("df.mean(1)")
    print(df.mean(axis=1))
    
    print("------------------------------------------------------------------")
    print("Operating with objects that have different dimensionality and need alignment.")
    print("In addition, pandas automatically broadcasts along the specified dimension.")
    print("------------------------------")
    s = pd.Series([1, 3, 5, np.nan, 6, 8], index=dates) 
    print("s = pd.Series([1, 3, 5, np.nan, 6, 8], index=dates)")
    print(s)
    print("------------------------------")
    # Series.shift():シフトにより空白になった要素NaNになる
    s = s.shift(2)
    print("s = pd.Series([1, 3, 5, np.nan, 6, 8], index=dates).shift(2)")
    print(s)
    print("------------------------------")
    df1 = df.sub(s, axis='index')
    # DataFrame.sub():引き算
    print("df.sub(s, axis='index')")
    print(df1)
    
    print("------------------------------------------------------------------")
    print("Applying functions to the data:")
    print("------------------------------")
    df1 = df.apply(np.cumsum)
    print("df.apply(np.cumsum)")
    print(df1)
    print("------------------------------")
    df1 = df.apply(lambda x: x.max() - x.min())
    print("df.apply(lambda x: x.max() - x.min())")
    print(df1)
    
    print("------------------------------------------------------------------")
    print("Histgramming")
    print("------------------------------")
    # randint(low, high=None, size=None, dtype='l')
    s = pd.Series(np.random.randint(0, 7, size=10))
    print("pd.Series(np.random.randint(0, 7, size=10))")
    print(s)
    print("------------------------------")
    s1 = s.value_counts()
    print("s.value_counts()")
    print(s1)
    print("------------------------------")
    print("s.value_counts().sort_index()")
    print(s1.sort_index())
    
    print("------------------------------------------------------------------")
    print("Series is equipped with a set of string processing methods in the str attribute ")
    print("that make it easy to operate on each element of the array, as in the code snippet below. ")
    s2 = pd.Series(['A', 'B', 'C', 'Aaba', 'Baca', np.nan, 'CABA', 'dog', 'cat'])
    print("------------------------------")
    print("pd.Series(['A', 'B', 'C', 'Aaba', 'Baca', np.nan, 'CABA', 'dog', 'cat'])")
    print(s2)
    print("------------------------------")
    print("s.str.lower()")
    print(s2.str.lower())
    