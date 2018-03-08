from random import randint

#part1
data = [randint(0,20) for _ in range(20)]

c = dict.fromkeys(data, 0) #fromkeys()用于创建一个新字典
print(c)

for x in data:
    c[x] += 1
print(c)
print(data)

#part2
from collections import Counter
c2 = Counter(data)

print(c2[10])
print(c2)
print(c2.most_common(3))

#part3
d = {x:randint(80,100) for x in 'abcxyz'}
print(d)
print(sorted(d))
print(d.keys())
print(d.values())
print(zip(d.values(), d.keys()))
print(sorted(zip(d.values(), d.keys())))
#print(zip(d.itervalues(), d.iterkeys()))
#print(sorted(zip(d.itervalues(), d.iterkeys())))
print(d.items())
print(sorted(d.items(), key = lambda x:x[1]))
print(sorted(d.items(), key = lambda x:x[1], reverse = True))