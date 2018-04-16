import numpy
import math
from numpy import fromstring
# x = numpy.array([[1,2],[3,4],[5,6]])
# print(x[[0,1]][:])
# k = numpy.arange(9,5,-0.2)
# print(k)
# m = k.reshape((3,3))
# print(m)
# x= numpy.array([['a','n',1],['b','c',2]])
# print(x,x.ndim,x.shape,x.size)
# x = numpy.array([[['a,','n',1],['v','g',2]],[['a,','n',1],['v','g',2]]])
# x.reshape(1,3,4)
# print(x)
# def f(x,y):
#     return (x,y)
# def g(x,y):
#     return x+y
# if __name__ == "__main__":
#     (x,y) = numpy.fromfunction(f,(3,3))
#     print(x,y)
# a = numpy.array([(1,2,3),(4,5,6)],float)
# # c = numpy.ones_like(a)
# # print(a[0][0])
# a = numpy.array([0])
# c = numpy.std(a)
# b = math.sqrt(2/9)
#
# print(c,b)
import numpy as np
x = np.arange(-2,2)
y = np.arange(0,3)
X,Y = np.meshgrid(x,y)     #生成3*4的矩阵,向下扩展
print(np.meshgrid(x,y))

# mgrid[[1:3:3j, 4:5:2j]]
# 3j：3个点
#
# 步长为复数表示点数，左闭右闭
# 步长为实数表示间隔，左闭右开

a,b = np.mgrid[0:5,0:5]
m,n = np.mgrid[0:5:5j,0:4:4j]    #生成5*4的矩阵，向右扩展
print(type(np.mgrid[0:5,0:5]))