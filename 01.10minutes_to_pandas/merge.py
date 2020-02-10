# coding: utf-8

import numpy as np
import pandas as pd

##################################################
# メイン
##################################################
if __name__ == '__main__':
    
    print("------------------------------------------------------------------")
    print("Concatenating pandas objects together with concat():")
    print("------------------------------")
    df = pd.DataFrame(np.random.randn(10, 4))
    print("pd.DataFrame(np.random.randn(10, 4))")
    print(df)
    print("------------------------------")
    print("break it into pieces")
    print("------------------------------")
    pieces = [ df[:3], df[3:7], df[7:] ]
    print("[ df[:3], df[3:7], df[7:] ]")
    for piece in pieces:
        print(piece)
    print("------------------------------")
    df1 = pd.concat(pieces)
    print("pd.concat([ df[:3], df[3:7], df[7:] ])")
    print(df1)
    
    print("------------------------------------------------------------------")
    print("SQL style merges. See the Database style joining section.")
    print("------------------------------")
    left = pd.DataFrame( {'key': ['foo', 'bar'], 'lval': [1, 2]} )
    right = pd.DataFrame( {'key': ['foo', 'bar'], 'rval': [4, 5]} )
    print("left:")
    print(left)
    print("------------------------------")
    print("right:")
    print(right)
    print("------------------------------")
    df2 = pd.merge(left, right, on='key')
    print("pd.merge(left, right, on='key')")
    print(df2)
    
