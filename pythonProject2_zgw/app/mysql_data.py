#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import argparse
import os
import commands
import hashlib
import subprocess
import sys
import shutil
import MySQLdb
import MySQLdb.cursors

reload(sys)
sys.setdefaultencoding("utf-8")


class Log:
    @staticmethod
    def e(msg):
        print(Log.red + '[x]:' + msg + Log.end)

    @staticmethod
    def w(msg):
        print(Log.yellow + '[!]:' + msg + Log.end)

    @staticmethod
    def i(msg):
        print(Log.green + '[+]:' + msg + Log.end)

    @staticmethod
    def t(msg):
        print(Log.blue + '[-]:' + msg + Log.end)

    red = '\033[1;31m'
    green = '\033[1;32m'
    yellow = '\033[1;33m'
    blue = '\033[1;34m'
    end = '\033[00m'


class get_marketcode(object):

    def connectdb(self):
        Log.w("start to connect database")
        # 本地连接
        db = MySQLdb.connect(host='地址', port=端口, user='用户名', passwd='密码', db='数据库', charset='latin1')
        Log.e("connect success")
        return db

    def select_table(self, table, db):
        cursor = db.cursor()
        sql = 'SELECT code1,str1,str2 FROM ' + table
        cursor.execute(sql)
        # 打印数据
        Log.w("select database, results list:")
        results = cursor.fetchall()
        code1_info = dict()
        str1_info = dict()
        if results:
            for rec in results:
                print
                rec[0], rec[1], rec[2]
                code1_info.update({rec[1]: rec[0]})
                str1_info.update({rec[1]: rec[2]})
        Log.w("Get code1_info ALIAS:")
        for key, values in code1_info.items():
            print
            str(key) + "=" + str(values)
        Log.w("Get str1_info ALIAS:")
        for key, values in str1_info.items():
            print
            str(key) + "=" + str(values)
        cursor.close()
        return code1_info, str1_info

    def invokedb(self):
        # 连接数据库
        db = self.connectdb()
        product_table = "表名"
        info = self.select_table(product_table, db)
        # 关闭数据库
        db.close()
        return info

    def match(self, info, manufacturer):
        marketcode = info[manufacturer]
        Log.w("get info of " + manufacturer + ":")
        print
        manufacturer + "=" + str(marketcode)
        return marketcode