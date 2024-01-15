#个数可变的位置参数
def fun(*num):
    print(type(num))
    for item in num:
        print(item)

#调用
fun(10,20,30,40)
fun(10)
fun([12,3,4,1]) #实际上传递的是一个参数
#在调用时，参数前面加一个*，会将列表进行解包
fun(*[12,3,4,1])

#个数可变的关键字参数
def fun2(**para):
    print(type(para))
    for key,value in para.items():
        print(key,'--->',value)

#调用
fun2(name='devin',age=18,w=60) #关键字参数
d={'name':'devin','age':18,'w':60}
#fun2(d) #TypeError: fun2() takes 0 positional arguments but 1 was given
fun2(**d) #解包