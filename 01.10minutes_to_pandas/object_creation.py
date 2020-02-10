# coding: utf-8

import numpy as np
import pandas as pd

##################################################
# メイン
##################################################
if __name__ == '__main__':
    
    # Creating a Series by passing a list of values, letting pandas creagite a default integer index:
    # Series
    print("------------------------------------------------------------------")
    print("Creating a Series by passing a list of values, letting pandas create a default integer index:")
    s = pd.Series([1, 3, 5, np.nan, 6, 8])
    print(s)
    
    # Creating a DataFrame by passing a NumPy array, with a datetime index and labeled columns:
    # Pandas
    print("------------------------------------------------------------------")
    print("Creating a DataFrame by passing a NumPy array, with a datetime index and labeled columns:")
    dates = pd.date_range('20130101', periods=6)
    print(dates)
    
    # DataFrame1
    #   randn:標準正規分布による6x4の行列
    #   index:datesをインデックスにセット
    #   cloumns:'A','B','C','D'を列としてセット
    df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
    print(df)
    
    # Creating a DataFrame by passing a dict of objects that can be converted to series-like.
    # DataFrame2
    #   np.array([3] * 4, dtype='int32') : 3が4個の配列
    #   Categorical:順序の概念を持った変数
    print("------------------------------------------------------------------")
    print("Creating a DataFrame by passing a dict of objects that can be converted to series-like.")
    df2 = pd.DataFrame(
        {
            'A': 1.,
            'B': pd.Timestamp('20130102'),
            'C': pd.Series(1, index=list(range(4)), dtype='float32'),
            'D': np.array([3] * 4, dtype='int32'),
            'E': pd.Categorical(["test", "train", "test", "train"]),
            'F': 'foo'
        }
    )
    print(df2)
    
    # The columns of the resulting DataFrame have different dtypes.
    print("------------------------------------------------------------------")
    print("The columns of the resulting DataFrame have different dtypes.")
    print(df2.dtypes)
    
    
    