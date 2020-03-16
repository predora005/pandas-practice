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
        __year (int)   : 年
        __month (int)  : 月
        __day (int)    : 日
        __hour (int)   : 時
        __point (int)  : 地点番号
        __df(DataFrame): スクレイピングで取得したデータ
    """

    ##############################
    # コンストラクタ
    ##############################
    def __init__(self, year, month, day, hour, point):
        """コンストラクタ
        
        Args:
            year (int): 年
            month (int): 月
            day  (int): 日
            hour (int): 時
            point  (int): 地点番号
            
        Returns:
           HighriseWeatherdataScraping: 自分自身
        """
        
        self.__year = year
        self.__month = month
        self.__day = day
        self.__hour = hour
        self.__point = point
        
    ##############################
    # URLを取得する
    ##############################
    def __get_url(self, year, month, day, hour, point):
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
        
        url_first_half = "https://www.data.jma.go.jp/obd/stats/etrn/upper/view/hourly_usp.php?"
        url_second_half = "year={0:04d}&month={1:02d}&day={2:02d}&hour={3:d}&atm=&point={4:d}".format(year, month, day, hour, point)
        url = url_first_half + url_second_half
        
        return url
        
    ##############################
    # 地上の気象データをスクレイピングする
    ##############################
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
        
    ##############################
    # 指定気圧面の気象データをスクレイピングする
    ##############################
    def __scrape_mandatory_level_data(self, html):
        """指定気圧面の気象データをスクレイピングする。
        
        Args:
            html (Response object): request.getで取得したResponseオブジェクト
            
        Return:
            DataFrame: スクレイピングしたデータ
        """
        
        # BeautifulSoupでHTMLを解析
        soup = BeautifulSoup(html.content, "html.parser")
        
        # id='tablefix2'の<table>を抽出
        table2 = soup.find('table', id='tablefix2')
        
        # table2内の全thを抽出
        th_all2 = table2.find_all('th')
    
        # 列タイトルをリストに格納する
        table2_column = []
        for th in th_all2:
            table2_column.append(th.string)
        
        # <table>内の全trを抽出。
        tr_all2 = table2.find_all('tr')
        
        # 先頭のtrは抽出済みなので飛ばす
        tr_all2 = tr_all2[1:]
        
        # 行と列の個数を算出し、ndarrayを作成
        number_of_cols2 = len(table2_column)
        number_of_rows2 = len(tr_all2)
        table2_data = np.zeros((number_of_rows2, number_of_cols2), dtype=np.float32)
        
        # 各行のデータをndarrayに格納する
        for r, tr in enumerate(tr_all2):
            td_all = tr.find_all('td')
            for c, td in enumerate(td_all):
                try:
                    table2_data[r,c] = td.string
                except ValueError:
                    table2_data[r,c] = np.nan

        # 抽出したデータのDataFrameを生成する
        df2 = pd.DataFrame(data=table2_data, columns=table2_column)
        
        return df2
        
    ##############################
    # 高層の気象データをスクレイピングする
    ##############################
    def scrape_high_rise_weather_data(self):
        """高層の気象データをスクレイピングする。
        
        Returns:
            HighriseWeatherdataScraping: 自分自身
        """
        
        # 指定URLのHTMLデータを取得
        url = self.__get_url(self.__year, self.__month, self.__day, self.__hour, self.__point)
        html = requests.get(url)
        print(url)
        
        # BeautifulSoupでHTMLを解析
        df1 = self.__scrape_ground_data(html)
        df2 = self.__scrape_mandatory_level_data(html)
        
        # 地上の気象データと指定気圧面の気象データを
        # ひとつのDataFrameに結合する
        df2.columns = df1.columns.values
        
        self.__df = pd.concat([df1, df2])
        
        return self

    ##############################
    # 高層の気象データをスクレイピングする
    ##############################
    def write_to_csv(self, filepath):
        """高層の気象データをスクレイピングする。
        
        Args:
            html (Response object): request.getで取得したResponseオブジェクト
        """
        
        self.__df.to_csv(filepath)
        #print(self.__df)
        