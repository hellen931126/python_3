from random import randint
import timeit

#part 1 
data = [randint(-10, 10) for _ in range(10)]

def myfilter():
    return filter(lambda x : x >= 0, data)

def mygenerater(): 
    return [x for x in data if x >= 0]

filter_data_time = timeit.timeit(stmt = myfilter)
generater_data_time = timeit.timeit(stmt = mygenerater)

print("filter_data_time" , filter_data_time)
print("generater_data_time", generater_data_time)
#filter用时更少， python3和python2的timeit用法不同


#part 2
d = {x : randint(60, 100) for x in range(1,21)}
print(d)
print({k:v for k,v in d.items() if v>90})
