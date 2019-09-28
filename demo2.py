'''
-*- coding: utf-8 -*-
@Author  : LiZhichao
@Time    : 2019/4/29 19:35
@Software: PyCharm
@File    : demo2.py
'''
import csv

#向CSV文件中写入数据
def write_csv_demo1():#创建一个writer对象
    headers = ['username','age','height']#定义表头信息，列表或元组
    values = [
        ('张三',17,170),
        ('李四',18,180),
        ('王五',19,190)
    ]

    with open('classroom.csv','w',encoding='utf-8',newline='') as \
            fp:#encoding='utf-8'解决乱码，newline=''解决空行，默认newline='\n'
        writer = csv.writer(fp)#创建一个writer对象
        writer.writerow(headers)#writerow一次写入一行
        writer.writerows(values)#writerows一次写入多行

def write_csv_demo2():#以字典的方式写入数据
    headers = ['username', 'age', 'height']  # 定义表头信息，列表或元组
    values = [
        {'username':'张三', 'age':17,  'height':170},
        {'username':'李四', 'age':18,  'height':180},
        {'username':'王五', 'age':19,  'height':190}
    ]

    with open('classroom1.csv', 'w', encoding='utf-8', newline='') as \
            fp:  # encoding='utf-8'解决乱码，newline=''解决空行，默认newline='\n'
        writer = csv.DictWriter(fp,headers)  # 创建一个writer对象
        writer.writeheader()  # 写入表头数据时，需要调用writeheader方法
        writer.writerows(values)  # writerows一次写入多行

if __name__ == '__main__':
    write_csv_demo1()
    write_csv_demo2()