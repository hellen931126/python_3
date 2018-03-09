'''题目：某编程竞赛系统，对参赛选手编程解题进行计时，选手完成题目后，
把该选手解题用时记录到字典中，以便赛后按选手名查询成绩，答题用时越
短，成绩越优.) {'LiLei':(2,43), 'HanMeimei':(5,52), 'Jim':(1,39)...}

比赛结束后，需按照排名顺序依次打印选手成绩，如何实现？'''
#无序
d = {}
d['Jim'] = (1, 35)
d['Leo'] = (2, 37)
d['Bob'] = (3, 40)
for k in d: print(k)

#解决方法
#使用collections.OrderedDict，以OrderedDict替代内置字典Dict，依次将选手成绩存入OrderedDict
from collections import OrderedDict
d1 = OrderedDict()
d1['Jim'] = (1, 35)
d1['Leo'] = (2, 37)
d1['Bob'] = (3, 40)
for k in d1: print(k)

#解决题目
from time import time
from random import randint
from collections import OrderedDict

d2 = OrderedDict()
players = list('ABCDEFGH')
start = time()

for a in range(8):
    input() #模拟选手答题
    p = players.pop(randint(0, 7-a))
    end = time()
    print(a + 1, end - start)
    d[p] = (a + 1, end - start)
