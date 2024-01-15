'''
判断两个类是否属于同一个类型
使用 isinstance 还是 type
'''

class A:
    pass

class B(A):
    pass

b=B()

# isinstance 可以及逆行继承关系的判断
print(isinstance(b,B))
print(isinstance(b,A))

# type 判断的是类与类之间的引用地址是否相等，不判断是否有继承关系
# 创建出一个类之后，类存储在内存中，且存储地址是唯一的
print(type(b) is B)
print(type(b) is A)

print(type(b),A,B,b)

# 如果要进行类型判断不要用type，而是使用isinstance