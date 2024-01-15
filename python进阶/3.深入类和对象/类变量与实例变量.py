class A:
    #类变量
    b=1
    def __init__(self,x,y):    # self是指实例对象
        #实例变量
        self.x=x
        self.y=y

a=A(2,3)

#实例对象访问实例变量和类变量
print(a.x,a.y,a.b)

#类访问类变量
print(A.b)

#类访问实例变量：类不能访问实例变量
#print(A.x,A.y)

#使用类修改类变量并使用实例对象访问类变量
A.b=11
print(A.b)
print(a.b)

#使用实例对象修改类变量
a.b=100
print('类访问类属性：%d' % A.b,'实例对象访问类变量：%d' % a.b)
'''
实例对象修改b这个变量的时候会重新创建一个实例变量
类访问类属性还是原来的类属性
'''

#类变量可以共享于多个实例对象
c=A(3,5)
print(c.b)