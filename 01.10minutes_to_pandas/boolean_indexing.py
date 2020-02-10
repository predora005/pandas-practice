# coding: utf-8

import numpy as np
import pandas as pd

##################################################
# メイン
##################################################
if __name__ == '__main__':
    
    dates = pd.date_range('20130101', periods=6)
    df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
    
    print("------------------------------------------------------------------")
    print("df:")
    print(df)
    
    print("------------------------------------------------------------------")
    print("Using a single column’s values to select data.")
    index1 = df['A'] > 0
    print("------------------------------")
    print("df['A'] > 0")
    print(index1)
    print("------------------------------")
    print("df[df['A'] > 0]")
    print(df[index1])
    
    print("------------------------------------------------------------------")
    print("Selecting values from a DataFrame where a boolean condition is met.")
    index2 = df > 0
    print("------------------------------")
    print("df > 0")
    print(index2)
    print("------------------------------")
    print("df[df> 0]")
    print(df[index2])
    
    print("------------------------------------------------------------------")
    print("Using the isin() method for filtering:")
    df2 = df.copy()
    df2['E'] = ['one', 'one', 'two', 'three', 'four', 'three']
    index3 = df2['E'].isin(['two', 'three', 'six'])
    print("------------------------------")
    print("df2")
    print(df2)
    print("------------------------------")
    print("df2['E'].isin(['two', 'three', 'six'])")
    print(index3)
    print("------------------------------")
    print("df[df2['E'].isin(['two', 'three', 'six'])]")
    print(df[index3])
            
    
    