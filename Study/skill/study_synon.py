import synonyms
a = "“我走过的桥比你走过的路还长”，现在大概很少有人用这口吻教训后生小子了!"
b = " 人生一世自然都要经过无数的桥，除了造桥的工程人员外，恐怕要算画家见的桥最多了。"
c = synonyms.compare(a,b)
print(c,'+++++++++++++++++++')
a = '中华上     下五千年。'
b = '长江水长十万里。'
c = synonyms.compare(a,b)
print(c,'-------------------')

from CilinSimilarity.source.cilin import CilinSimilarity

cl = CilinSimilarity()
sim = cl.similarity('人脸','脸部')
print(sim)
sim = cl.sim2013('人脸','脸部')
print(sim)
sim = cl.sim2016('人脸','人脸')
print(sim)

a = [[1,2,3,4],[1,2,3,4,5,6]]
b = 0
c = 0
for i in a:
    for j in i:
        b += j
        c += 1
print(b,'++++')
print(b/c)
m = [sum(i)/len(i)for i in a]
print(sum(m),'++++++++')
print(sum(m)/len(m))
