class Student:
    def __init__(self,student_list):
        self.student=student_list
    
    #魔法函数
    def __getitem__(self,item):
        return self.student[item] 

    def __str__(self):
        return ','.join(self.student)
    def __repr__(self):
        return ','.join(self.student)


'''
魔术方法是python定义的方法
魔术方法的名称不能随意更改
对当前这个类进行了功能拓展

item 索引 index
从0开始,直到python运行抛出异常,自动结束for循环
'''
student=Student(['顾安','夏洛','大海'])
for i in student:
    print(i)

#当使用print进行实例化对象打印时，自动调用__str__方法
print(student)

#调试模式
student


'''
当前的魔术方法是不是因为继承了object而拥有的这些方法 答案：错误
当前的魔法方法是python自带的，跟类没有关系
魔术方法是自带的，不能自己去实现魔术方法
'''


#绝对值
class Nums:
    def __init__(self,num):
        self.num=num
    
    def __abs__(self):
        return abs(self.num)
    
my_num=Nums(-3)
print(abs(my_num))


#向量运算
class myVector:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __add__(self,other_instance):
        re_vector=myVector(self.x+other_instance.x,self.y+other_instance.y)
        return re_vector
    
    def __str__(self):
        return f'x:{self.x}, y:{self.y}'
    
vec_1=myVector(1,2)
vec_2=myVector(2,3)

print(vec_1+vec_2)
