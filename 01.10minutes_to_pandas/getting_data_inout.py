# coding: utf-8

import numpy as np
import pandas as pd

##################################################
# メイン
##################################################
if __name__ == '__main__':
    
    df = pd.DataFrame(
        np.random.randn(1000, 4), 
        index=pd.date_range('1/1/2000', periods=1000), 
        columns=['A', 'B', 'C', 'D']
    )
    
    print("----------------------------------------")
    print("CSV")
    print("----------------------------------------")
    df.to_csv('foo.csv')
    
    read_csv_df = pd.read_csv('foo.csv')
    print("[df.read_csv('foo.csv')]")
    print(read_csv_df)
    
    print("----------------------------------------")
    print("HDF5")
    print("----------------------------------------")
    df.to_hdf('foo.h5', 'df')
    read_h5_df = pd.read_hdf('foo.h5', 'df')
    print("[pd.read_hdf('foo.h5', 'df')]")
    print(read_h5_df)
    
    print("----------------------------------------")
    print("Excel")
    print("----------------------------------------")
    df.to_excel('foo.xlsx', sheet_name='Sheet1')
    # header:どの行をcolumnsにするか、index=col:どの列をindexにするか
    read_xlsx_df = pd.read_excel(
        'foo.xlsx', sheet_name='Sheet1', header=None, index_col=None, na_values=['NA'])
    print("[pd.read_excel('foo.xlsx', sheet_name='Sheet1')]")
    print(read_xlsx_df)
        