from dbfread import DBF,FieldParser
from time import sleep
import chardet,re
import string
# char_decode_errors

def SBC2DBC(ustring):
    rstring = ""
    for uchar in ustring:
        inside_code = ord(uchar)
        if inside_code == 0x0020:
            inside_code = 0x3000
        else:
            if not (0x0021 <= inside_code and inside_code <= 0x7e):
                rstring += uchar
                continue
            inside_code += 0xfee0
        rstring += chr(inside_code)
    return rstring

table = DBF(r"E:\QQ文件\现代汉语词典.dbf",encoding="cp936",recfactory=None,char_decode_errors="ignore")
records = []
table=table._iter_records
for record in table:
    recordss = record[0][1].replace(" ","").replace("[","")
    records.append(recordss)
c =0
upper = string.ascii_letters
print(upper)
for i in records:
    if "B" in upper and SBC2DBC("B") in i :
        print(i)
        c += 1/len(i)
print(c)


