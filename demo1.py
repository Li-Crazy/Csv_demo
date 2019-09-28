'''
-*- coding: utf-8 -*-
@Author  : LiZhichao
@Time    : 2019/4/28 19:43
@Software: PyCharm
@File    : demo1.py
'''
import csv

def read_csv_demo1():
    with open('stock.csv','r') as fp:
        reader = csv.reader(fp)#reader是一个迭代器,以列表形式
        next(reader)#从第一行数据开始读取，不从第零行读取
        for x in reader:
            # print(x)
            name = x[3]
            volumn = x[-1]
            print({'name':name,'volumn':volumn})

def read_csv_demo2():
    with open('stock.csv','r') as fp:
        reader = csv.DictReader(fp)#DictReader以有序字典形式返回,不包含标题行
        for x in reader:
            value = {"名称":x['名称'],"成交笔数":x['成交笔数']}
            print(value)


if __name__ == '__main__':
    # read_csv_demo1()
    read_csv_demo2()