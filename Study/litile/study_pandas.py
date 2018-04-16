import pandas as pd
import numpy as np
from pandas import Series,DataFrame

# ser = Series(np.arange(3.))
# print(ser)
# data = DataFrame(np.arange(16).reshape(4,4),index=list('abcd'),columns=list('wxyz'))
# print(data['w'])  #选择表格中的'w'列，使用类字典属性,返回的是Series类型
# print(type(data.w))
# print(type(data[['w']]))
# print(data[['w','z']])
# print(np.arange(16).reshape(2,2,2,2))
# s = Series([100,"PYTHON","Soochow","Qiwsir"])
# print(s.values)
# data = {"name":["yahoo","google","facebook"],"marks":[200,400,600],"price":[9,3,7]}
# f3 = DataFrame(data,columns=["name","marks","price","debt"],index=["A","B","C"])
# print(f3.index)
# obj6 = Series([3,-1,4,2,1])
#
# c = Series(['c','a','d','a','a','b','b','c','c']).value_counts()
# for i in c:
#     print(i)
# df = DataFrame(np.arange(12).reshape((4,3)),index=[['a','a','b','b'],[1,2,1,2]],columns=[['Ohio','Ohio','Colorado'],['Green','Red','Green']])
# d = df.sortlevel(1)
# print(d)
# print(df[df>2])
# print(df.ix[1])

data = DataFrame(np.arange(16).reshape(4,4),index=['a','b','c','d'],columns=['A','B','C','D'])
print(data[data>5])