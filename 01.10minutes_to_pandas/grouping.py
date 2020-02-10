# coding: utf-8

import numpy as np
import pandas as pd

##################################################
# メイン
##################################################
if __name__ == '__main__':
    
    df = pd.DataFrame({'A': ['foo', 'bar', 'foo', 'bar',
                             'foo', 'bar', 'foo', 'foo'],
                       'B': ['one', 'one', 'two', 'three',
                             'two', 'two', 'one', 'three'],
                       'C': np.random.randn(8),
                       'D': np.random.randn(8)})
    print("------------------------------------------------------------------")
    print("df:")
    print(df)
    
    print("------------------------------------------------------------------")
    print("Grouping and then applying the sum() function to the resulting groups.")
    print("------------------------------")
    df1 = df.groupby('A').sum()
    print("df.groupby('A').sum()")
    print(df1)
    print("------------------------------")
    df2 = df.groupby('B').sum()
    print("df.groupby('B').sum()")
    print(df2)
    
    print("------------------------------------------------------------------")
    print("Grouping and then applying the sum() function to the resulting groups.")
    print("------------------------------")
    df3 = df.groupby(['A', 'B']).sum()
    print("df.groupby(['A', 'B']).sum()")
    print(df3)

