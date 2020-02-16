# coding: utf-8

import numpy as np
import pandas as pd

df = pd.read_csv('csv/foo1.csv')
print(df)

df = pd.read_csv('csv/foo2.csv', header=None)
print(df)

df = pd.read_csv('csv/foo3.csv', sep='\t')
print(df)

df = pd.read_csv('csv/foo4.csv', header=[0,1])
print(df)

df = pd.read_csv('csv/foo2.csv', names=['a','b','c','d','e'])
print(df)

df = pd.read_csv('csv/foo5.csv', index_col=0)
print(df)

df = pd.read_csv('csv/foo5.csv', index_col='A')
print(df)

df = pd.read_csv('csv/foo6.csv', index_col=[0,1])
print(df)

df = pd.read_csv('csv/foo6.csv', index_col=['A','B'])
print(df)

df = pd.read_csv('csv/foo5.csv', usecols=[1,2])
print(df)

df = pd.read_csv('csv/foo5.csv', usecols=['A','E'])
print(df)

df = pd.read_csv('csv/foo5.csv', usecols=lambda s: s < 'C')
print(df)

df = pd.read_csv('csv/foo7.csv')
print(df)
print(df.columns)

df = pd.read_csv('csv/foo7.csv', skipinitialspace=True)
print(df)
print(df.columns)

df = pd.read_csv('csv/foo8.csv')
print(df)

df = pd.read_csv('csv/foo8.csv', skiprows=[0,1])
print(df)

df = pd.read_csv('csv/foo9.csv')
print(df)

df = pd.read_csv('csv/foo9.csv', na_values=['-','NG'])
print(df)

df = pd.read_csv('csv/foo10.csv')
print(df)
print(df.dtypes)

df = pd.read_csv('csv/foo10.csv', parse_dates=[0])
print(df)
print(df.dtypes)

df = pd.read_csv('csv/foo10.csv', parse_dates=['date'])
print(df)
print(df.dtypes)

print('----')
df = pd.read_csv('csv/foo11.csv')
print(df)
print(df.dtypes)

print('----')
print()

df = pd.read_csv('csv/foo11.csv', 
                 dtype={'no': np.int64, 'name': object, 
						'age': np.int64, 'height': 'float64'} )
print(df)
print(df.dtypes)
