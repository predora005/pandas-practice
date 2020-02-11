# coding: utf-8

import numpy as np
import pandas as pd


##################################################
# 天気情報CSVファイル読み込み
##################################################
def read_weather_csv(filepath):
    
    read_csv_df = pd.read_csv(filepath, sep=',', skiprows=3, header=[0,1,2], index_col=0)
    return read_csv_df

##################################################
# 天気情報CSVデータから気温取り出し
##################################################
def extract_temperature(df):
    return df['気温(℃)'].iloc[:,0]

##################################################
# 天気情報CSVデータから降水量取り出し
##################################################
def extract_rainfall(df):
    return df['降水量(mm)'].iloc[:,0]

##################################################
# 天気情報CSVデータから天気取り出し
##################################################
def extract_weather(df):
    return df['天気'].iloc[:,0]

##################################################
# メイン
##################################################
if __name__ == '__main__':
    
    filepath = '~/input/train/mito/mito_20170101-20170115data.csv'
    
    # CSVファイル読み込み
    mito_df = read_weather_csv(filepath)
    print(mito_df)
    
    # --------------------------------------------------
    # 天気データのNaNを補間する
    #   - 前方補間
    #   - 補間しきれなかったNaNは後方補間(前方補間だと最初の方がNaNのまま)
    # --------------------------------------------------
    mito_df = mito_df.fillna(method='ffill')
    mito_df = mito_df.fillna(method='bfill')
    print(mito_df)
    
    # --------------------------------------------------
    # 気温,降水量,天気を取り出し
    # --------------------------------------------------
    print("[気温]")
    print(extract_temperature(mito_df))
    
    print("[降水量]")
    print(extract_rainfall(mito_df))
        
    print("[天気]")
    print(extract_weather(mito_df))
        
    