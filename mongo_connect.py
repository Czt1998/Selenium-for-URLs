# encoding=utf8
"""

"""
from pymongo import MongoClient
import datetime
import requests
import os

def data_save(datas):
    connection = MongoClient('192.168.235.55', 27017)
    db = connection.admin
    db.authenticate("admin","123456")
    db = connection.team_behind_sc
    post_sub = db.Filmmaker_page
    post_sub.save(datas)

if __name__ == '__main__':
    datas = None
    data_save(datas)



