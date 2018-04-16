import numpy as np

a = np.array([1,2,3,4,5,6])   #生成一维数组
print(a,a.dtype)
b = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
b[5:8] = 12    #如上面展示的，NumPy数组和Python列表最重要的一点在于，数组切片是原始数组的视图，数据不会被复制，在视图上进行的任何修改都会直接反映到源数组上！
print(b)
print(b - 1)
c = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(c[:1][:1])
print(c[0:1,0:1])


print("--------------------------------------------------------------------------------")
names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
data = np.random.randn(7,4)
print(data)
print(names == "Bob")
print(data[names == "Bob"])