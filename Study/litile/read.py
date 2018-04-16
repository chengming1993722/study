# path = r'E:\QQ文件\20180202四套语文教科书处理版\人教版1~9年级\人民教育出版社-七年级-上册（课文）\散步'
# with open(path,encoding='utf8') as f :
#     lines = f.readlines()
#     print(lines)
from xlrd import open_workbook,xldate_as_tuple
data = open_workbook(r"E:\QQ文件\总词汇表.xls")
table = data.sheets()[0]
c = 0
cats = []
for row in range(table.nrows):
    if c == 0:
        c += 1
        continue
    cat = table.row_values(row)[3].lstrip('(').rstrip(')').split('、')
    for i in cat:
        if i not in cats:
            cats.append(i)
print(cats)