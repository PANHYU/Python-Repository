# class A:
#     name='A'

#     def __init__(self):
#         self.name='obj'

# a=A()
# print(a.name)



# '''
# 类的多继承的查找顺序
#     深度优先
#     广度优先
# '''

# #深度优先
# class E:
#     pass

# class D:
#     pass

# class C(E):
#     pass

# class B(D):
#     pass

# class A(B,C):
#     pass

# #通过mro方法进行查找顺序的查看
# print(A.__mro__)


#广度优先
class D:
    pass

class C(D):
    pass

class B(D):
    pass

class A(B,C):
    pass

print(A.__mro__)


'''
不同的继承关系可以调用不同的搜索方式
    C3算法

类在不同的继承关系中有不同的调用顺序
    什么时候调用深度优先
    什么时候调用广度优先

mro 进行查找顺序的查看
'''
