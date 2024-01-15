def happy_birthday(name='devin',age='18'):
    print('祝'+name+'生日快乐')
    print(str(age)+'岁生日快乐')

#调用
happy_birthday() #不用传参
happy_birthday(name='kailong')
happy_birthday(age=19)
# happy_birthday(19) #TypeError: can only concatenate str (not "int") to str

def fun(a,b=20): #a作为位置参数，b作为默认值参数
    pass

#def fun2(a=20,b): #报错：语法错误   当位置参数和默认值参数同时存在的时候，位置参数在后会被报错
    pass
#                  当位置参数和关键字参数同时存在的时候，应该遵循位置参数在前，默认值参数在后