'''
题目：很多应用程序都有浏览用户的历史记录的功能，例如，浏览器可以查看最近访问过的网页。
视频播放器可以查看最近播放过的视频文件。Shell可以查看用户输入过的命令……

现在我们制作了一个简单的猜数字的小游戏，添加历史记录功能，显示用户最近猜过的数字，如何实现？
'''
from random import randint

N = randint(0, 100)

#这里对python2版本的if-else进行了改进，去掉了else
def guess(k):
    if k == N:
        print('right')
        return True
    if k < N:
        print('%s is less than N' % k)
        return False
    print('%s is greater than N' % k)
    return False

while True:
    line = input('please enter a number: ')
    if line.isdigit():
        k = int(line)
        if guess(k):
            break


#添加历史记录功能（只显示最近五次的历史记录）：
#使用容量为n的队列存储历史记录。使用标准库collections中的deque，它是一个双端循环队列。

from collections import deque
from random import randint

history = deque([], 5) #第一个参数为初始值，第二个参数为数组容量

N = randint(0, 100)

def guess(k):
    if k == N:
        print('right')
        return True
    if k < N:
        print('%s is less than N' % k)
        return False
    print('%s is greater than N' % k)
    return False

while True:
    line = input('please enter a number: ')
    if line.isdigit():
        k = int(line)
        history.append(k)
        if guess(k):
            break
    elif line == 'history' or line == 'h?':
        print(list(history))


