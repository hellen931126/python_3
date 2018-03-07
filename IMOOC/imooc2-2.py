# Name each element in the tuple to improve code readability

NAME, AGE, SEX, EMAIL = range(4)

student = ('Jim', '16', 'male', 'jim8721@gmail.com')
print(student[NAME])


from collections import namedtuple
Student = namedtuple('Student',['name','age','sex','email'])
s = Student('Jim', '16', 'male', 'jim8721@gmail.com')

print(s)
print(s.name)
print(s.age)
print(isinstance(s, tuple))