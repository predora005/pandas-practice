# coding: utf-8

import numpy as np
import pandas as pd

##################################################
# メイン
##################################################
if __name__ == '__main__':

    # Here is how to view the top and bottom rows of the frame:
    print("------------------------------------------------------------------")
    print("Here is how to view the top and bottom rows of the frame:")
    dates = pd.date_range('20130101', periods=6)
    df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
    print("------------------------------")
    print("df.head():")
    print(df.head())
    print("------------------------------")
    print("df.tail(3):")
    print(df.tail(3))
    
    # Display the index, columns:
    print("------------------------------------------------------------------")
    print("Display the index, columns:")
    print("------------------------------")
    print("df.index:")
    print(df.index)
    print("------------------------------")
    print("df.columns:")
    print(df.columns)

    # DataFrame.to_numpy() gives a NumPy representation of the underlying data. 
    print("------------------------------------------------------------------")
    print("DataFrame.to_numpy() gives a NumPy representation of the underlying data. ")
    df2 = pd.DataFrame({
            'A': 1.,
            'B': pd.Timestamp('20130102'),
            'C': pd.Series(1, index=list(range(4)), dtype='float32'),
            'D': np.array([3] * 4, dtype='int32'),
            'E': pd.Categorical(["test", "train", "test", "train"]),
            'F': 'foo'
    })
    print("------------------------------")
    print("df.to_numpy():")
    print(df.to_numpy())
    print("------------------------------")
    print("df2.to_numpy():")
    print(df2.to_numpy())

    # describe() shows a quick statistic summary of your data: 
    print("------------------------------------------------------------------")
    print("describe() shows a quick statistic summary of your data:")
    print(df.describe())

    # Transposing your data:
    print("------------------------------------------------------------------")
    print("Transposing your data:")
    print(df.T)

    # Sorting by an axis:
    #   sort_index:行名や列名でソートする
    print("------------------------------------------------------------------")
    print("Sorting by an axis:")
    print("------------------------------")
    print("df.sort_index(axis=0, ascending=False):")
    print(df.sort_index(axis=0, ascending=False))
    print("------------------------------")
    print("df.sort_index(axis=1, ascending=False):")
    print(df.sort_index(axis=1, ascending=False))

    # Sorting by values:
    #   sort_index:行名や列名でソートする
    print("------------------------------------------------------------------")
    print("Sorting by values:")
    print("------------------------------")
    print("df.sort_values(by='B')")
    print(df.sort_values(by='B', ascending=True))
