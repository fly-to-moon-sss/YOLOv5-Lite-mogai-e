import os

path = "labels/"

# 获取该目录下所有文件，存入列表中
fileList = os.listdir(path)
alldata = []
for i in fileList:
    with open(path + i, "r") as f:  # 打开文件
        data = f.readlines()  # 读取文件
        alldata.append(data)
        for j in data:
            # print(j)
            if j[0] == '0' or j[0] == '1'or j[0] == '2'or j[0] == '3'or j[0] == '4'or j[0] == '5'or j[0] == '6'or j[0] == '7'or j[0] == '8'or j[0] == '9':
                continue
            else:
                print(i)