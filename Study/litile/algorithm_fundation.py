def shunxu_search(a_list,items):
    pos = 0
    found = False
    while pos < len(a_list) and not found:
        print(pos)
        if a_list[pos] == items:
            found = True
        else:
            pos = pos+1
    return found

def binary_search(a_list,item):
    first = 0
    last = len(a_list)-1
    found = False
    while first <= last and not found:
        mid = (first+last)//2
        if a_list[mid] == item:
            found = True
        else:
            if item < a_list[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return found


class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None]*self.size
        self.data = [None]*self.size

    def put_data_in_slots(self,key,data,slot):
        if self.slots[slot] == None:
            self.slots[slot] = key
            self.data[slot] = data
            return True
        else:
            if self.slots[slot] == key:
                self.slots[slot] = data
                return True
            else:
                return False
    def put(self,key,data):
        slot = self.hash_function(key,self.size)
        result = self.put_data_in_slots(key,data,slot)
        while not result:
            slot = self.rehash(slot,self.size)
            result = self.put_data_in_slots(key,data,slot)

    def hash_function(self,key,size):
        return key % size

    def rehash(self,old_hash,size):
        return (old_hash + 1) % size

    def get(self,key):
        start_slot = self.hash_function(key,len(self.slots))
        print(start_slot)
        data = None
        stop = False
        found = False
        pos = start_slot
        while self.slots[pos] != None and not found and not stop:
            if self.slots[pos] == key:
                found = True
                data = self.data[pos]
            else:
                pos = self.rehash(pos,len(self.slots))
                if pos == start_slot:
                    stop = True
        return data

    def __getitem__(self,key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key,data)


if __name__ == '__main__':
    table=HashTable()
    table[54]='cat'
    table[26]='dog'
    table[16]='lion'
    table[93]="tiger"
    table[77]="bird"
    table[44]="goat"
    table[55]="pig"
    table[20]="chicken"
    print (table.slots)
    print(table.data)
    print(table[16])



# if __name__ == '__main__':
#     test_list = [1, 2, 32, 8, 17, 19, 42, 13, 0]
#     print(shunxu_search(test_list,3))
#     print(shunxu_search(test_list,13))