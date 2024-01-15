def happy_birthday(name,age):
    print('祝'+name+'生日快乐')
    print(str(age)+'岁生日快乐')
#调用
#happy_birthday('pan') #TypeError: happy_birthday() missing 1 required positional argument: 'age'
#happy_birthday(18,'Kailong') #TypeError: can only concatenate str (not "int") to str
happy_birthday('Kailong',18)