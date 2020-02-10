# coding: utf-8

import numpy as np
import pandas as pd

##################################################
# メイン
##################################################
if __name__ == '__main__':
    
    print("------------------------------------------------------------------")
    print("Stack")
    print("------------------------------")
    print("array:")
    array1 = [   ['bar', 'bar', 'baz', 'baz', 'foo', 'foo', 'qux', 'qux'],
                ['one', 'two', 'one', 'two', 'one', 'two', 'one', 'two'] ]
    print(array1)
    print("------------------------------")
    print("zip(*array)")
    for i in zip(*array1):
        print(i)
    print("------------------------------")
    tuples = list(zip(*array1))
    print("tuples = list(zip(*array))")
    print(tuples)
    print("------------------------------")
    index = pd.MultiIndex.from_tuples(tuples, names=['first', 'second'])
    print("pd.MultiIndex.from_tuples(tuples, names=['first', 'second'])")
    print(index)
    print("------------------------------")
    df = pd.DataFrame(np.random.randn(8, 2), index=index, columns=['A', 'B'])
    print("pd.DataFrame(np.random.randn(8, 2), index=index, columns=['A', 'B'])")
    print(df)
    print("------------------------------")
    df2 = df[:4]
    print("df2 = df[:4]")
    print(df2)
    
    print("------------------------------------------------------------------")
    print("The stack() method “compresses” a level in the DataFrame’s columns.")
    print("------------------------------")
    stacked = df2.stack()
    print("stacked = df2.stack()")
    print(stacked)
    
    print("------------------------------------------------------------------")
    print("With a “stacked” DataFrame or Series (having a MultiIndex as the index), ")
    print("the inverse operation of stack() is unstack(), ")
    print("which by default unstacks the last level:")
    print("------------------------------")
    unstacked = stacked.unstack()
    print("unstacked = stacked.unstack()")
    print(unstacked)
    print("------------------------------")
    unstacked2 = stacked.unstack(2)
    print("unstacked2 = stacked.unstack(2)")
    print(unstacked2)
    print("------------------------------")
    unstacked1 = stacked.unstack(1)
    print("unstacked1 = stacked.unstack(1)")
    print(unstacked1)
    print("------------------------------")
    unstacked0 = stacked.unstack(0)
    print("unstacked0 = stacked.unstack(0)")
    print(unstacked0)
    
    print("------------------------------------------------------------------")
    print("Pipot tables")
    print("------------------------------")
    df = pd.DataFrame({'A': ['one', 'one', 'two', 'three'] * 3,
                       'B': ['1', '2', '1'] * 4,
                       'C': ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'] * 2,
                       #'D': np.random.randn(12),
                       #'E': np.random.randn(12)})
                       'D': np.arange(12),
                       'E': np.arange(12,24)})
    print("df:")
    print(df)
    print("------------------------------")
    print("We can produce pivot tables from this data very easily:")
    print("------------------------------")
    pivot_table = pd.pivot_table(df, values='D', index=['A', 'B'], columns=['C'], aggfunc=np.sum)
    print("pd.pivot_table(df, values='D', index=['A', 'B'], columns=['C'], aggfunc=np.sum)")
    print(pivot_table)
    
    