from random import randint, sample

print(sample('abcdefg', 3))
print(sample('abcdefg', randint(3,6)))

s1 = {x:randint(1,4) for x in sample('abcdefg', randint(3,6))}
print('s1:', s1)
s2 = {x:randint(1,4) for x in sample('abcdefg', randint(3,6))}
print('s2:', s2)
s3 = {x:randint(1,4) for x in sample('abcdefg', randint(3,6))}
print('s3:', s3)

#keys()，在python2里用的是viewkeys()
print(s1.keys())
print(s1.items())
print(s1.values())
#get the intersection of 3 sets
print('public keys:', s1.keys() & s2.keys() & s3.keys())

#map(), reduce()
from functools import reduce #python2可直接使用reduce

print(map(dict.keys, [s1, s2, s3]))
print(reduce(lambda a, b : a & b, map(dict.keys, [s1, s2, s3])))