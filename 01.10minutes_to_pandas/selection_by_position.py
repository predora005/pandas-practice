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
    print("Select via the position of the passed integers:")
    print("------------------------------")
    print("df.iloc[3]")
    print(df.iloc[3])
    
    print("------------------------------------------------------------------")
    print("By integer slices, acting similar to numpy/python:")
    print("------------------------------")
    print("df.iloc[3:5, 0:2]")
    print(df.iloc[3:5, 0:2])
    
    print("------------------------------------------------------------------")
    print("By lists of integer position locations, similar to the numpy/python style:")
    print("------------------------------")
    print("df.iloc[ [1, 2, 4], [0, 2] ]")
    print(df.iloc[ [1, 2, 4], [0, 2] ])
        
    print("------------------------------------------------------------------")
    print("For slicing rows explicitly:")
    print("------------------------------")
    print("df.iloc[1:3, :]")
    print(df.iloc[1:3, :])
        
    print("------------------------------------------------------------------")
    print("For slicing columns explicitly:")
    print("------------------------------")
    print("df.iloc[: 1:3]")
    print(df.iloc[:, 1:3])
        
    print("------------------------------------------------------------------")
    print("For getting a value explicitly:")
    print("------------------------------")
    print("df.iloc[1, 1]")
    print(df.iloc[1, 1])
        
    print("------------------------------------------------------------------")
    print("For getting fast access to a scalar (equivalent to the prior method):")
    print("------------------------------")
    print("df.iat[1, 1]")
    print(df.iat[1, 1])
        
    
    
    
    