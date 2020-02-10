# coding: utf-8

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

##################################################
# メイン
##################################################
if __name__ == '__main__':
    
    
    print("------------------------------------------------------------------")
    print("We use the standard convention for referencing the matplotlib API:")
    print("----------------------------------------")
    plt.close('all')
    ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
    ts = ts.cumsum()
    ts.plot()
    plt.savefig('fig1.png')
    
    print("------------------------------------------------------------------")
    print("On a DataFrame, the plot() method is a convenience to plot all of the columns with labels:")
    print("----------------------------------------")
    df = pd.DataFrame(
        np.random.randn(1000, 4), 
        index=pd.date_range('1/1/2000', periods=1000), 
        columns=['A', 'B', 'C', 'D']
    )
    df = df.cumsum()
    
    # プロット領域の作成
    #   (1x1), figsizeの単位はインチ
    fig, axes = plt.subplots(1, 1, figsize=(8,6))
    
    # DataFrameを指定したAxesにセットする
    df.plot(ax=axes)
    
    # 凡例をセットする
    #   locは位置。'best'='upper right'.
    plt.legend(loc='best')
    
    # 表示する
    plt.show()
    
    # ファイルに保存する
    plt.savefig('fig2.png')
    
        
    
    