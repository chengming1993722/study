# decode_set = ["utf-8","gb18030","ISO-8859-2","gb2312","gbk","Error"]
# for k in decode_set:
#     try:
#         file = open(r"E:\QQ文件\现代汉语词典.dbf","r",encoding=k)
#         readfile = file.read()
#         print("open file r'E:\QQ文件\现代汉语词典.dbf' with encoding %s"%k)
#         readfile = readfile.encode(encoding="utf-8",errors="replace")
#         break
#     except:
#         if k == "Error":
#             raise Exception("r'E:\QQ文件\现代汉语词典.dbf'had no way to decode")
table = open(r'E:\QQ文件\现代汉语词典.dbf',"r")
print(table)
for recode in table:
    recode=recode.decode("cp936").encode("utf8")
    print(recode)
