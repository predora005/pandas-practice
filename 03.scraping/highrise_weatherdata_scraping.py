# coding: utf-8

import numpy as np
import pandas as pd

import requests
from bs4 import BeautifulSoup

##################################################
# 高層の気象データをスクレイピングするクラス。
##################################################
class HighriseWeatherdataScraping:
    """高層の気象データをスクレイピングするクラス。
    

    Attributes:
        属性の名前 (属性の型): 属性の説明
        属性の名前 (:obj:`属性の型`): 属性の説明.
    """
    
    
    ###################################
    ##################################################
    def __init__(self, fruit_id):
        """コンストラクタ
        
        Args:
            引数の名前 (引数の型): 引数の説明
            引数の名前 (:obj:`引数の型`, optional): 引数の説明.

        Returns:
           戻り値の型: 戻り値の説明 (例 : True なら成功, False なら失敗.)
        """
        self.fruit_id = fruit_id
        self.fruit_name = self.get_fruit_name(fruit_id=fruit_id)
        self.price_dict = self.get_price_dict(fruit_id=fruit_id)
        
        
    def __get_url(year, month, day, hour, point):
        """ URLを取得する。
        
        Args:
            year (int): 年
            month (int): 月
            day  (int): 日
            hour (int): 時
            point  (int): 地点番号
            
        Returns:
            string: URL
        """
        
        #url = "https://www.data.jma.go.jp/obd/stats/etrn/upper/view/hourly_usp.php?year=2017&month=01&day=01&hour=9&atm=&point=47646"
        url_first_half = "https://www.data.jma.go.jp/obd/stats/etrn/upper/view/hourly_usp.php?"
        url_second_half = "year={0:04d}&month={1:02d}&day={2:02d}&hour={3:d}&atm=&point={4:d}".format(year, month, day, hour, point)
        url = url_first_half + url_second_half
        
    def __scrape_ground_data(self, html):
        """地上の気象データをスクレイピングする。
        
        Args:
            html (Response object): request.getで取得したResponseオブジェクト
            
        Return:
            DataFrame: スクレイピングしたデータ
        """
        
        # BeautifulSoupでHTMLを解析
        soup = BeautifulSoup(html.content, "html.parser")
        
        # id='tablefix1'の<table>を抽出し、table1内の全thを抽出
        table1 = soup.find('table', id='tablefix1')
        th_all = table1.find_all('th')

        # 列タイトルをリストに格納する
        table1_column = []
        for th in th_all:
            table1_column.append(th.string)
        
        # <table>内の全trを抽出。先頭のtr(列タイトル)は抽出済みなので飛ばす
        tr_all = table1.find_all('tr')[1:]

        # 行と列の個数を算出し、ndarrayを作成
        number_of_cols = len(table1_column)
        number_of_rows = len(tr_all)
        table1_data = np.zeros((number_of_rows, number_of_cols))
        
        # 各行のデータをndarrayに格納する
        for r, tr in enumerate(tr_all):
            td_all = tr.find_all('td')
            table1_data[r,:] = [td.string for td in td_all]

        # 抽出したデータのDataFrameを生成する
        df = pd.DataFrame(data=table1_data, columns=table1_column)
        
        return df
        
    def scrape_high_rise_weather_data(self):
        """高層の気象データをスクレイピングする。
        
        Args:
            引数の名前 (引数の型): 引数の説明
            引数の名前 (:obj:`引数の型`, optional): 引数の説明.
        
        Returns:
            DataFrame: スクレイピングしたデータ
        """
        
        # 年月日・時刻・地点情報
        year = 2017
        month = 1
        day = 1
        hour = 9
        point = 4764    # 館野
        
        # 指定URLのHTMLデータを取得
        url = self.__get_url(year, month, day, hour, point)
        html = requests.get(url)
        
        
        ## BeautifulSoupでHTMLを解析

