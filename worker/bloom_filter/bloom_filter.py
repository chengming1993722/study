from particple import segments,major_segments,minor_segments
class BloomFilter(object):
    def __init__(self,size):
        self.values = [False]*size
        self.size = size

    def hash_value(self,value):
        return hash(value)%self.size

    def add_value(self,value):
        h = self.hash_value(value)
        self.values[h] = True

    def might_contain(self,value):
        h = self.hash_value(value)
        return self.values[h]

    def print_contents(self):
        print(self.values)


class Splunk(object):
    def __init__(self):
        self.bf = BloomFilter(64)
        self.terms ={}
        self.events = []

    def add_event(self,event):
        event_id = len(self.events)
        self.events.append(event)
        for term in segments(event):
            self.bf.add_value(term)
            if term not in self.terms:
                self.terms[term] = set()
                print(self.terms)
            self.terms[term].add(event_id)

    def search(self,term):
        if not self.bf.might_contain(term):
            return
        if term not in self.terms:
            return
        for event_id in sorted(self.terms[term]):
            yield self.events[event_id]

s = Splunk()
s.add_event('src_ip = 1.2.3.4')
s.add_event('src_ip = 5.6.7.8')
s.add_event('dst_ip = 1.2.3.4')
for event in s.search('1.2.3.4'):
    print (event)
print('-')
for event in s.search('src_ip'):
    print (event)
print("-")
for event in s.search('ip'):
    print (event)





# bf = BloomFilter(10)
# bf.add_value('dog')
# bf.add_value('fish')
# bf.add_value('cat')
# bf.print_contents()
# bf.add_value('bird')
# bf.print_contents()
# for term in ['dog','fish','cat','bird','duck','emu']:
#     print('{}:{}{}'.format(term,bf.hash_value(term),bf.might_contain(term)))
#
# print(hash("bird,cat"),hash("bird")+hash("cat"))
