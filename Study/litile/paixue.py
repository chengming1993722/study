import re
from time import sleep
# def tryint(s):
#     try:
#         return int(s)
#     except:
#         return s
#
# def alphanum_key(s):
#     return [tryint(c) for c in re.split('([0-9]+)',s) ]
#
#
#
#
# if __name__ =="__main__":
#     a=['S31S10_new', 'S31S11_new', 'S31S12_new', 'S31S8_new', 'S31S9_new']
#     a.sort(key=lambda v:alphanum_key(v))

# odd = lambda x : bool(x%2)
# numbers = [i for i in range(10)]
# numbers = [(n,print(n)) for n in numbers if not odd(n)][:]
# print(numbers)
# print(locals())

def selection_sort(a_list):
    for fill_slot in range(len(a_list) - 1, 0, -1):
        print(fill_slot)
        pos_of_max = 0
        for location in range(1, fill_slot + 1):
            if a_list[location] > a_list[pos_of_max]:
                pos_of_max = location
        a_list[fill_slot],a_list[pos_of_max]=a_list[pos_of_max],a_list[fill_slot]


# a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
# selection_sort(a_list)
# print(a_list)

def insertion_sort(a_list):
    for index in range(1, len(a_list)):
        current_value = a_list[index]
        print(current_value)
        position = index
        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position = position - 1
        a_list[position] = current_value


def insertion_sort_binarysearch(a_list):
    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index
        low=0
        high=index-1
        while low<=high:
            mid=(low+high)//2
            if a_list[mid]>current_value:
                high=mid-1
            else:
                low=mid+1
        while position > low:
            a_list[position] = a_list[position - 1]
            position = position -1
        a_list[position] = current_value


a_list = [54, 26, 93, 15, 77, 31, 44, 55, 20]
insertion_sort(a_list)
print(a_list)
insertion_sort_binarysearch(a_list)
print(a_list)