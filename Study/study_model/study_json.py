import json
'''
# Python 字典类型转换为 JSON 对象
data = {
    'no' : 1,
    'name' : 'Runoob',
    'url' : 'http://www.runoob.com '
}

##json_str = json.dumps(data)
##print ("Python 原始数据：", type(repr(data)))
##print ("JSON 对象：", type(json_str))

with open(r'D:\Study\study_model\data.json',"w") as f:
    json.dump(data,f)

#读取.json文件
with open(r'D:\Study\study_model\data.json',"r") as f:
    data1 = json.load(f)
    print(data1)
##pprint() from pprint import pprint
'''
'''
s = '{"name": "ACME", "shares": 50, "price": 490.1}'
from collections import OrderedDict
data = json.loads(s, object_pairs_hook=OrderedDict)
print(data)
#output:OrderedDict([('name', 'ACME'), ('shares', 50), ('price', 490.1)])
class JsonObject:
    def __init__(self,d):
        self.__dict__ = d
data1 = json.loads(s,object_hook=JsonObject)
#>>>data1.name
#output: 'ACME'
#>>>data1.shares
#output: 50
'''
'''
class Piont:
    def __init__(self,x,y):
        self.x=x
        self.y=y

#数列化实例对象
def serialize_instance(obj):
    d = {'__classname__':type(obj).__name__}
    print(d)
    d.update(vars(obj))
    return d

#获取实例
classes = {
'Piont':Piont
    }
def unserialize_object(d):
    print(d)
    clsname = d.pop('__classname__',None)
    if clsname:
        cls = classes[clsname]
        obj = cls.__new__(cls) #Make without calling __init__
        for key,value in d.items():
            setattr(obj,key,value)
        return obj
    else:
        return d

>>> p=Piont(2,3)
>>> s=json.dumps(p,default=serialize_instance )
{'__classname__': 'Piont'}
>>> s
'{"__classname__": "Piont", "x": 2, "y": 3}'
>>> a = json.loads(s,object_hook = unserialize_object)
{'__classname__': 'Piont', 'x': 2, 'y': 3}
>>> a
<__main__.Piont object at 0x03E3C830>
>>> a.x
2

'''



    
    





























