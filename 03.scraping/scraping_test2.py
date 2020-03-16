# coding: utf-8

from scraping.highrise_weatherdata_scraping import HighriseWeatherdataScraping

##################################################
# メイン
##################################################
if __name__ == '__main__':
    
    # 年月日・時刻・地点情報
    year = 2017
    month = 1
    day = 1
    hour = 9
    point = 47646   # 館野
    
    # 高層の気象データスクレイピングクラスを作成する
    highriseWeather = HighriseWeatherdataScraping(year, month, day, hour, point)
    
    # スクレイピングを実行する。
    highriseWeather.scrape_high_rise_weather_data().write_to_csv("test.csv")
    
