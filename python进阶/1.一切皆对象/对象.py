def print_name(name='Bob'):
    print(name)

# my_func=print_name
# my_func()
# my_func('Devin')

class Person:
    def __init__(self):
        print('Alen')

# my_class=Person
# my_class()

#可以将对象传递给集合对象中
obj_list=[]
obj_list.append(print_name)
obj_list.append(Person)

# for item in obj_list:
#     print(item())


#将函数当成返回值
def decorator_func():
    print('start...')
    return print_name

#装饰器的用法
my_func_feturn=decorator_func()
my_func_feturn('Amy')



#将函数作为参数传递给另外一个函数
def a(age):
    print(age)

def b(func):
    return func

c=b(a)
c(18)
