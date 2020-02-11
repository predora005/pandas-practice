# coding: utf-8

import os
import numpy as np
import pandas as pd

##################################################
# 指定したディレクトリの天気情報CSVファイルを
# 読み込み、ひとつのDataFrameに結合して返す
##################################################
def read_weather_csvs(dir_path):
    
    # --------------------------------------------------
    # sortedを使用してファイル名の昇順に読み込む
    # --------------------------------------------------
    file_paths = []
    for file_name in sorted(os.listdir(dir_path)):
        
        # ディレクトリの場合はpass
        if os.path.isdir(dir_path + '/' + file_name):
            continue
        
        # 拡張子が一致したらリストに追加
        base,ext = os.path.splitext(file_name)
        if ext == '.csv':
            file_paths.append(dir_path + '/' + file_name)
    
    # --------------------------------------------------
    # CSVファイルから天気情報を読み込む
    # --------------------------------------------------
    read_csv_dfs = []
    for file_path in file_paths:
        read_csv_df = pd.read_csv(file_path, sep=',', skiprows=3, header=[0,1,2], index_col=0)
        read_csv_dfs.append(read_csv_df)
    
    # --------------------------------------------------
    # 読み込んだデータを結合する
    # --------------------------------------------------
    df = pd.concat(read_csv_dfs)
    
    return df

##################################################
# 天気情報CSVファイル読み込み
##############tep####################################
def read_weather_csv(file_path):
    read_csv_df = pd.read_csv(file_path, sep=',', skiprows=3, header=[0,1,2], index_col=0)
    return read_csv_df

##################################################
# 天気情報CSVデータの天気データのNanを補間する
#   - 前方補間
#   - 補間しきれなかったNaNは後方補間(前方補間だと最初の方がNaNのまま)
##################################################
def fill_weather(df):
    filled_df = df.fillna(method='ffill')
    filled_df.fillna(method='bfill', inplace=True)
    return filled_df

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

    