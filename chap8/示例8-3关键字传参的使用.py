def happy_birthday(name,age):
    print('祝'+name+'生日快乐')
    print(str(age)+'岁生日快乐')

#调用
happy_birthday(age=18,name='kailong') #必须和形参保持一致
happy_birthday('devin',age=18) #位置传参和关键字传参可以同时使用
#happy_birthday(name='sha',18) 
'''SyntaxError: positional argument follows keyword argument
位置传参要在关键字传参的前面'''