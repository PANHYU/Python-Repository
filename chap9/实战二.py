class Student:
    def __init__(self,name,age,gender,score):
        self.name=name
        self.age=age
        self.gender=gender
        self.score=score
    
#实例方法
    def info(self):
        print(self.name,self.age,self.gender,self.score)
    
print('请输入5位学生的信息：（姓名#年龄#性别#成绩）')
lst=[] #用于存储5位学生对象
for i in range(1,6):
    s=input(f'请输入第{i}位学生的信息及成绩：')
    s_lst=s.split('#') #索引为0的是姓名，索引为1的是年龄，索引为2的是性别，索引为3的是成绩
    #创建学生对象
    stu=Student(s_lst[0],s_lst[1],s_lst[2],s_lst[3])
    #将学生对象添加到列表中
    lst.append(stu)

#遍历列表，调用学生对象的info方法
for item in lst: #item的数据类型是Student类型
    item.info() #对象名.方法名()