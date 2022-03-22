# 1. 目標頁面:https://cn.investing.com/equities/apple-computer-inc-historical-data
# 2. 製作該頁的歷史股價爬蟲
# 3. 提供的Function要能夠選擇抓取的時間範圍
# 4. 輸出請用JSON_ARRAY

# pip install lxml

import requests
import pandas as pd
import json
from bs4 import BeautifulSoup

def aaplJson(st_date,end_date):
          url = 'https://cn.investing.com/instruments/HistoricalDataAjax'
          headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                    "AppleWebKit/537.36 (KHTML, like Gecko)"
                    "Chrome/63.0.3239.132 Safari/537.36"
               ,'referer': 'https://cn.investing.com/equities/apple-computer-inc-historical-data'
               ,'content-type': 'application/x-www-form-urlencoded'
               ,'x-requested-with': 'XMLHttpRequest'}
          data = {'curr_id': '6408'
          ,'smlID': '1159963'
          ,'header': 'AAPL历史数据'
          ,'st_date': st_date
          ,'end_date': end_date
          ,'interval_sec': 'Daily'
          ,'sort_col': 'date'
          ,'sort_ord': 'DESC'
          ,'action': 'historical_data'}

          re = requests.post(url=url,data=data,headers = headers)

          tb = pd.read_html(re.text)
          table = tb[0]
          
          records = table.to_json(orient='index')
     
          return records


json.loads(aaplJson('2021/06/01','2021/07/22'))

