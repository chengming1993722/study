# -*- coding: utf-8 -*-
import os
import xlwt,xlrd
import xlsxwriter

def change():
    path1 = r'E:\QQ文件\20180202'
    workbook = xlsxwriter.Workbook(r'E:\reference.xlsx')
    worksheet = workbook.add_worksheet('Sheet1')
    i = 0
    for lx,file1 in enumerate(os.listdir(path1)):
        new_path1 = os.path.join(path1,file1)
        x = str(lx+1)
        for ly,file2 in enumerate(os.listdir(new_path1)):
            new_path2 = os.path.join(new_path1,file2)
            y = str(ly+1)
            for ln,file3 in enumerate(os.listdir(new_path2)):
                new_path3 = os.path.join(new_path2,file3)
                n = str(ln+1)
                new_path4 = os.path.join(new_path2,n)
                os.rename(new_path3,new_path4)
                worksheet.write(i,0,x)
                worksheet.write(i,1,file1)
                worksheet.write(i,2,y)
                worksheet.write(i,3,file2)
                worksheet.write(i,4,n)
                worksheet.write(i,5,file3)
                i += 1
            new_path5 = os.path.join(new_path1,y)
            os.rename(new_path2,new_path5)
        new_path6 = os.path.join(path1,x)
        os.rename(new_path1,new_path6)
    workbook.close()

def transform():
    path = r'E:\reference.xlsx'
    data = xlrd.open_workbook(path)
    table = data.sheets()[0]
    matters = []
    mirrors = []
    for row in range(table.nrows):
        matter = [table.row_values(row)[0],table.row_values(row)[2],table.row_values(row)[4]]
        mirror = [table.row_values(row)[1],table.row_values(row)[3],table.row_values(row)[5]]
        matters.append(matter)
        mirrors.append(mirror)
    path1 = r'E:\QQ文件\20180202'
    for file1 in os.listdir(path1):
        newpath1 = os.path.join(path1,file1)
        ln = None
        for file2 in os.listdir(newpath1):
            newpath2 = os.path.join(newpath1,file2)
            lm = None
            for file3 in os.listdir(newpath2):
                newpath3 = os.path.join(newpath2,file3)
                nums = [file1,file2,file3]
                inx = matters.index(nums)
                essay = mirrors[inx]
                newpath4 = os.path.join(newpath2,essay[2])
                os.rename(newpath3,newpath4)
                lm = essay[1]
                ln = essay[0]
            newpath5 = os.path.join(newpath1,lm)
            os.rename(newpath2,newpath5)
        newpath6 = os.path.join(path1,ln)
        os.rename(newpath1,newpath6)

if __name__=='__main__':
    change()
    # transform()