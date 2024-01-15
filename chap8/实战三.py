#方法一
def lower_upper(x):
    lst=[]
    for item in x:
        if 'A'<=item<='Z':
            lst.append(chr(ord(item)+32)) #ord()将字母转成Unicode码整数，加上32，chr()将整数码转成字符
        elif 'a'<=item<='z':
            lst.append(chr(ord(item)-32))
        else:
            lst.append(item)
    return ''.join(lst)

#调用
s=input('请输入一个字符串：')
new_s=lower_upper(s)
print(new_s)

#方法二
# def lower_upper(x):
#     lst=[]
#     for item in x:
#         if 'A'<=item<='Z':
#             lst.append(item.lower()) #ord()将字母转成Unicode码整数，加上32，chr()将整数码转成字符
#         elif 'a'<=item<='z':
#             lst.append(item.upper())
#         else:
#             lst.append(item)
#     return ''.join(lst)

# #调用
# s=input('请输入一个字符串：')
# new_s=lower_upper(s)
# print(new_s)