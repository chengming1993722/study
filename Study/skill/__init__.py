#-*- coding：utf-8 -*-
import csv
import xlrd
import chardet
# path = r'E:\QQ文件\测试文本'
# path1 = r'E:\QQ文件\文本分析\数据摆放的格式范例.xlsx'
# data = xlrd.open_workbook(path1)
# table = data.sheets()[0]
# header = table.row_values(0)
# headers = []
# for i in header:
#     i.encode('utf-8')
#     headers.append(i)
# with open(path,'w',encoding='utf-8') as f:
#     f_csv = csv.writer(f)
#     f_csv.writerow(header)
# a = open(path,encoding='utf-8')
# print(len(a.readlines()))
# f = open(path,'rb')
# data = f.read()
# encoding = (chardet.detect(data))['encoding']
# f.close()
# with open(path,encoding=encoding,newline='') as f:
#     lines = f.readlines()
#     print(len(lines))
#     for line in lines:
#         line.encode('utf-8')
#         print(line)
import zipfile
path = r'E:\测试课文.zip'
def un_zip(path):
    zip_files = zipfile.ZipFile(path)
    for f in zip_files.filelist:
        f.filename = f.filename.encode('cp437').decode('gbk')
        print(f.filename)
        zip_files.extract(f)
un_zip(path)