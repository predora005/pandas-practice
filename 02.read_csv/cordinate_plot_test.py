# coding: utf-8

import read_weather_csv as rwc
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2
import math

##################################################
# 緯度・経度を画面座標に変換する
##################################################
def convert_cordinates_map_to_screen(
    latitude, longitude, 
    max_latitude, max_longitude,
    max_screen_height, max_screen_width):
        
    screen_height =  max_screen_height * latitude  / max_latitude
    screen_width  =  max_screen_width  * longitude / max_longitude
    
    return (int(screen_height), int(screen_width))
    
##################################################
# 気象値をRGBに変換する
##################################################
def convert_value_to_rgb(value, min_value, max_value):
    
    color_code = [
        (  0,  32, 128),    (  0,  65, 255),    (  0, 150, 255),
        (185, 235, 255),    (255, 255, 240),    (255, 255, 150),
        (250, 245,   0),    (255, 153,   0),    (255,  40,   0),
        (180, 0, 104)
    ]
    
    len_color_code = len(color_code)
    number_of_boundary = len_color_code - 2
    
    # インデックスを求める
    index = number_of_boundary * (value - min_value) / (max_value - min_value) + 1
    if index < 0:
        index = 0
    if index > (len_color_code - 1):
        index = (len_color_code - 1)
    index = int(index)

    return color_code[index]

##################################################
# 線形補間する
##################################################
def get_linear_interpolated_values(screen_cordinates, values, screen_width, screen_height):
    
    value_array = np.zeros(shape=(screen_width, screen_width))
    num_values = len(values)
    
    for w in range(screen_width):
        for h in range(screen_width):
            
            # 各地点と、補間したい点との距離を求める
            no_interpolate = False
            sum_of_inv_distance = 0
            inv_distances = {}
            for point_name in screen_cordinates:
                
                pw, ph = screen_cordinates[point_name]
                
                # 座標が完全一致したら直接代入する
                if (w == pw) and (h == ph):
                    value_array[pw, ph] = values[point_name]
                    no_interpolate = True
                    break
                
                # 距離を求める
                distance = math.sqrt((w - pw)**2 + (h - ph)**2)
                inv_distances[point_name] = 1 / distance
                sum_of_inv_distance += 1/ distance
            
            # 補間不要ならcontinue
            if no_interpolate:
                continue
            
            # 補間値を設定する
            value_array[w,h] = 0
            for point_name in screen_cordinates:
                pw, ph = screen_cordinates[point_name]
                value = values[point_name]
                inv_distance = inv_distances[point_name]
                
                #rate = (sum_of_distance - distance) / sum_of_distance
                rate = inv_distance / sum_of_inv_distance
                value_array[w,h] += value * rate
                #print(w, h, point_name, value, rate)

    return value_array
    
##################################################
# メイン
##################################################
if __name__ == '__main__':
    
    # 地点
    points = [
        {   'name': '水戸',
            'dir_path': '/home/ec2-user/input/train/mito/',
            'latitude' : 36.34139,
            'longitude': 140.44667,
        },
        {   'name': '東京',
            'dir_path': '/home/ec2-user/input/train/tokyo/',
            'latitude': 35.689521,
            'longitude': 139.691704
        },
        {   'name': '秩父',
            'dir_path': '/home/ec2-user/input/train/chichibu/',
            'latitude': 35.9898194,
            'longitude': 139.0731637
        }
    ]
    
    # 緯度と経度の範囲
    START_LONGITUDE = 138.390038
    END_LONGITUDE = 140.831191
    START_LATITUDE = 34.921678
    END_LATITUDE = 37.151276
    MAX_LATITUDE = END_LATITUDE - START_LATITUDE
    MAX_LONGITUDE = END_LONGITUDE - START_LONGITUDE
    
    # 画面の大きさ
    MAX_SCREEN_WIDTH = 128
    MAX_SCREEN_HEIGHT = 128
    
    # --------------------------------------------------
    # 指定してディレクトリのCSVファイルから
    # 天気情報を取得する
    # --------------------------------------------------
    dfs = {}
    for point in points:
        # CSVから読み込み
        dir_path = point['dir_path']
        csv_df = rwc.read_weather_csvs(dir_path)
        
        # 読み込んだデータをディクショナリに格納
        point_name = point['name']
        dfs[point_name] = csv_df

    # --------------------------------------------------
    # 気温を取得する
    # --------------------------------------------------
    temperature_df = pd.DataFrame()
    for key in dfs:
        df = dfs[key]
        temperature = rwc.extract_temperature(df)
        temperature_df[key] = temperature

    # --------------------------------------------------
    # 緯度・経度を画面座標に変換する
    # --------------------------------------------------
    screen_cordinates = {}
    for point in points:
        point_name = point['name']
        latitude = point['latitude']
        longitude = point['longitude']
        
        # 緯度・経度を画面座標に変換する
        screen_h, screen_w = convert_cordinates_map_to_screen(
            latitude - START_LATITUDE, longitude - START_LONGITUDE, 
            MAX_LATITUDE, MAX_LONGITUDE,
            MAX_SCREEN_HEIGHT, MAX_SCREEN_WIDTH)
            
        screen_cordinates[point_name] = (screen_w, screen_h)
        
        #print(point_name, screen_w, screen_h, temperature_df[point_name][0])
    
    
    # --------------------------------------------------
    # 各画面座標の気温を線形補間で求める
    # --------------------------------------------------
    value_array = get_linear_interpolated_values(
        screen_cordinates, temperature_df.iloc[0], 
        MAX_SCREEN_WIDTH, MAX_SCREEN_HEIGHT)
    
    # --------------------------------------------------
    # 気温をRGBに変換する
    # --------------------------------------------------
    rgb_array = np.zeros(shape=(MAX_SCREEN_WIDTH, MAX_SCREEN_HEIGHT, 3))
    for i in range(value_array.shape[0]):
        for j in range(value_array.shape[1]):
            temperature = value_array[i,j]
            r, g, b = convert_value_to_rgb(temperature, -5, 35)
            rgb_array[i, j] = (b, g, r)
            #print(i, j, temperature, (r, g, b))

    
    cv2.imwrite('test.png', rgb_array)
