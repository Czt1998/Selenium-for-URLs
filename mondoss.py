# -*- coding:utf-8 -*-
from pymongo import MongoClient
import datetime
import os

def data_save(datas):
    print(datas)
    connection = MongoClient()
    post_info = connection.team_behind_sc
    post_sub = post_info.Filmmaker_page
    # 連接數據庫
    post_sub.save(datas)

if __name__ == '__main__':
    datas = None
    data_save(datas)




