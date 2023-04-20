import os
import random
import numpy as np
from numpy import *

txt_file_path = 'labels-1'  # 原始的标签路径
save_file_path = 'labels-2'  # 修改后的标签路径

labels_name = os.listdir(txt_file_path)  # 获得每一个标签名字的列表 / os.listdir() 方法用于返回指定的文件夹包含的文件或文件夹的名字的列表
num = len(labels_name)  # 获取列表长度
list = range(num)  # 创建从0到num的整数列表  list = range(0, num)
files = os.listdir(save_file_path)

for i in list:  # 遍历每一个文件
    name = labels_name[i]  # 获取每一个文件的文件名
    read_file = open(txt_file_path + "/" + name, 'r')  # 读取txt_file_path/labels路径中的文件，r表示以只读方式打开文件
    fline = read_file.readlines()  # 读取txt文件中每一行 / readlines()表示读取整行 / fline是列表类型，fline列表里的元素是str类型
    save_txt = open(save_file_path + "/" + name,
                    'w+')  # 读取save_file_path/labels路径中的文件. w+表示打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。

    for j in fline:  # 遍历txt文件中每一行
        list1 = j.split()
        # print(list1)

        # 删除类别
        if list1[0] != '2':  # 删除类别1
            if list1[0] != '3':  # 删除类别2
                if list1[0] != '4':  # 删除类别2
                    if list1[0] != '5':  # 删除类别2
                        if list1[0] != '6':  # 删除类别2
                            list2 = list1
                            # print(list2)

                            # 修改类别
                            if list2[0] == '7':
                                list2[0] = '2'  # 将类别3改成类别1


                b = " ".join(list2)  # 将列表转换成字符串类型，且用空格分割
                save_txt.write(b)  # 写入新的文件中
                save_txt.write('\n')  # 换行