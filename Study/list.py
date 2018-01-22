from math import exp,log,sqrt
import re
from datetime import datetime,date,time,timedelta
from operator import itemgetter
import sys,os,glob

# my_list=[[123,2,2,444],[22,6,6,444],[354,4,4,678],[236,5,5,678],[236,5,5,290],[461,1,1,290]]
# my_list_sorted_by_index_3_and_0=sorted(my_list,key=itemgetter(3,0))
# print("Output #92:{}".format(my_list_sorted_by_index_3_and_0))
# input_file = sys.argv[1]
# filerader = open(input_file,"r")
# for c in filerader:
#     print(c)
# filerader.close()
# inputPath = sys.argv[1]
# for input_file in glob.glob(os.path.join(inputPath,'*.txt')):
#     with open(input_file,"r") as filerader:
#         for row in filerader:
#             print("{}".format(row.strip()))

# my_letters=['a','b','c','d','e','f','g','h','i','j']
# max_index=len(my_letters)
# output_file=sys.argv[1]
# filewriter=open(output_file,"w")
# print(output_file)
# for index_value in range(len(my_letters)):
#     if index_value < (max_index-1):
#         filewriter.write(my_letters[index_value]+"\t")
#     else:
#         filewriter.write(my_letters[index_value]+"\n")
#         print("OK")
# filewriter.close()
class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

s = Student()
s.score = 60


