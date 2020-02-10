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
    
    # Selecting a single column, which yields a Series, equivalent to df.A:
    print("------------------------------------------------------------------")
    print("Selecting a single column, which yields a Series, equivalent to df.A:")
    print("------------------------------")
    print("df['A']:")
    print(df['A'])
    
    # Selecting via [], which slices the rows.
    print("------------------------------------------------------------------")
    print("Selecting via [], which slices the rows.")
    print("------------------------------")
    print("df[0:3]")
    print(df[0:3])
    print("------------------------------")
    print("df['20130102': '20130104']")
    print(df['20130102': '20130104'])
    print("------------------------------")
    print("df[3:]")
    print(df[3:])
    
    print("------------------------------------------------------------------")
    print("For getting a cross section using a label:")
    print("------------------------------")
    print("df.loc[dates[0]]")
    print(df.loc[dates[0]])
    print("------------------------------------------------------------------")
    print("Selecting on a multi-axis by label:")
    print("------------------------------")
    print("df.loc[:, ['A', 'B'] ]")
    print(df.loc[:, ['A', 'B'] ])
    print("------------------------------------------------------------------")
    print("Showing label slicing, both endpoints are included:")
    print("------------------------------")
    print("df.loc['20130102':'20130104', ['A', 'B'] ]")
    print(df.loc['20130102':'20130104', ['A', 'B'] ])
    print("------------------------------------------------------------------")
    print("Reduction in the dimensions of the returned object:")
    print("------------------------------")
    print("df.loc['20130102', ['A', 'B'] ]")
    print(df.loc['20130102', ['A', 'B'] ])
    print("------------------------------------------------------------------")
    print("For getting a scalar value:")
    print("------------------------------")
    print("df.loc[dates[0], 'A']")
    print(df.loc[dates[0], 'A'])
    print("------------------------------------------------------------------")
    print("For getting fast access to a scalar (equivalent to the prior method):")
    print("------------------------------")
    print("df.at[dates[0], 'A']")
    print(df.at[dates[0], 'A'])

