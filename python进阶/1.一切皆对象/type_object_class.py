'''
type 可以创建一个类
class 声明一个类
object 所有类当中的基类
'''

'''
type可以创建python中的对象,python一切皆对象
type继承了object
object是通过type创建的
type是由自身创建的
'''

'''
type -> int -> object
'''
a=1
b='abc'
print(type(a))
print(type(int))
print(type(b))
print(type(str))

class Student:
    pass

stu=Student()
print(type(stu))
print(type(Student))
print(int.__bases__)
print(str.__bases__)
print(Student.__bases__)
print(type.__bases__)
print(object.__bases__)
print(type(object))
print(type(type))