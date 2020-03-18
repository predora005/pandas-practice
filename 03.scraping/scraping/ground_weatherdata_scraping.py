# coding: utf-8

import numpy as np
import pandas as pd

import requests
from bs4 import BeautifulSoup

##################################################
# 地上の気象データをスクレイピングするクラス。
##################################################
class GroundWeatherdataScraping:
    """地上の気象データをスクレイピングするクラス。
    
    Attributes:
        __prec_no(int) : 都道府県番号
        __block_no(int): 観測所番号
        __year (int)   : 年
        __month (int)  : 月
        __day (int)    : 日
        __df(DataFrame): スクレイピングで取得したデータ
    """

    ##############################
    # コンストラクタ
    ##############################
    def __init__(self, prec_no, block_no, year, month, day):
        """コンストラクタ
        
        Args:
            prec_no(int) : 都道府県番号
            block_no(int): 観測所番号
            year (int)   : 年
            month (int)  : 月
            day  (int)   : 日
            
        Returns:
           GroundWeatherdataScraping: 自分自身
        """
        
        self.__prec_no = prec_no
        self.__block_no = block_no
        self.__year = year
        self.__month = month
        self.__day = day
        
    ##############################
    # URLを取得する
    ##############################
    def __get_url(self, prec_no, block_no, year, month, day):
        """ URLを取得する。
        
        Args:
            prec_no(int): 都道府県番号
            block_no(int): 観測所番号
            year (int): 年
            month (int): 月
            day  (int): 日

        Returns:
            string: URL
        """
        
        # https://www.data.jma.go.jp/obd/stats/etrn/view/hourly_s1.php?prec_no=40&block_no=47629&year=2017&month=1&day=1&view=
        #url_second_half = "year={0:04d}&month={1:02d}&day={2:02d}&hour={3:d}&atm=&point={4:d}".format(year, month, day, hour, point)
        url_first_half = "https://www.data.jma.go.jp/obd/stats/etrn/view/hourly_s1.php?"
        url_second_half = "prec_no={0:d}&block_no={1:d}&year={2:d}&month={3:d}&day={4:d}".format(prec_no, block_no, year, month, day)
        url = url_first_half + url_second_half
        
        return url
        
    ##############################
    # 気象データをスクレイピングする
    ##############################
    def __scrape_data(self, html):
        """気象データをスクレイピングする。
        
        Args:
            html (Response object): request.getで取得したResponseオブジェクト

        Return:
            DataFrame: スクレイピングしたデータ
        """
        
        # BeautifulSoupでHTMLを解析
        soup = BeautifulSoup(html.content, "html.parser")
        
        # id=table_idの<table>を抽出
        table = soup.find('table', id="tablefix1")
        
        # table内の全trを抽出
        tr_all = table.find_all('tr')
        
        # テーブル見出しの行数をカウントする
        header_row_num = 0
        for tr in tr_all:
            th = tr.find('th')
            if th is not None:
                header_row_num = header_row_num + 1
            #print('=================================')
            #print(tr)
        
        # 最大列数を取得する
        max_col_num = 0
        for tr in tr_all:
            col_num = 0
            th_all = tr.find_all('th')
            if th_all is not None:
                for th in th_all:
                    rowspan = th.get('rowspan')
                    colspan = th.get('colspan')
                    if colspan is None:
                        col_num = col_num + 1
                    else:
                        col_num = col_num + int(colspan)
                    print('=================================')
                    print(th)
                    print(rowspan, colspan, col_num)
        
        
        
        # table内の全thを抽出
        #th_all = table.find_all('th')
        #th_tr_all = soup.select('table > tbody > th > tr')
        #th_tr_all = soup.select('table')
        #print(th_tr_all)
        #for tr in th_tr_all:
        #    print(tr)
        
        
        # 列タイトルをリストに格納する
        #table_column = []
        #for th in th_all:
        #    table_column.append(th.string)
        
        # <table>内の全trを抽出。
        #tr_all = table.find_all('tr')
        
        # 先頭のtrは抽出済みなので飛ばす
        #tr_all = tr_all[1:]
        
        # 行と列の個数を算出し、ndarrayを作成
        #number_of_cols = len(table_column)
        #number_of_rows = len(tr_all)
        #table_data = np.zeros((number_of_rows, number_of_cols), dtype=np.float32)
        
        # 各行のデータをndarrayに格納する
        #for r, tr in enumerate(tr_all):
        #    td_all = tr.find_all('td')
        #    for c, td in enumerate(td_all):
        #        try:
        #            table_data[r,c] = td.string
        #        except ValueError:
        #            table_data[r,c] = np.nan

        # 抽出したデータのDataFrameを生成する
        #df = pd.DataFrame(data=table_data, columns=table_column)
        
        #return df
        
    ##############################
    # 気象データをスクレイピングする
    ##############################
    def scrape_weather_data(self):
        """気象データをスクレイピングする。
        
        Returns:
            HighriseWeatherdataScraping: 自分自身
        """
        
        # 指定URLのHTMLデータを取得
        url = self.__get_url(self.__prec_no, self.__block_no, self.__year, self.__month, self.__day)
        html = requests.get(url)
        print(url)
        
        # BeautifulSoupでHTMLを解析
        self.__df = self.__scrape_data(html)
        
        return self
        
    ##############################
    # 気象データをスクレイピングする
    ##############################
    def write_to_csv(self, filepath):
        """気象データをスクレイピングする。
        
        Args:
            html (Response object): request.getで取得したResponseオブジェクト
        """
        
        self.__df.to_csv(filepath)
