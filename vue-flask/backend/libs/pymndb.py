import pymongo
import configparser
import os, sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

config = configparser.ConfigParser()
config.read(os.path.join(BASE_DIR, "config\config.ini"))


# print(config.sections())

class MongoDBClient:

    def __init__(self):
        self.host = config.get('MongoDB', 'host')
        self.port = config.get('MongoDB', 'port')


    #连接mongo数据库
    def connect(self):
        conn = pymongo.MongoClient(f"mongodb://{self.host}:{self.port}/")
        # print("----------conn----", conn)
        return conn

    #增
    def add_data(self):
        conn = self.connect()

    #删
    def del_data(self):
        conn = self.connect()

    #改
    def update_data(self):
        conn = self.connect()

    #查
    def all_data(self):
        conn = self.connect()
        db = conn.omy
        col = db.test
        all_data = col.find()

        return all_data

    #查询某一条数据
    def one_data(self):
        conn = self.connect()