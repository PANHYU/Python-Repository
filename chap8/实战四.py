def get_find(s,lst):
    for item in lst:
        if s==item:
            return True
    return False
#调用
lst=['hello','world','python']
s=input('请输入您要判断的字符串：')
result=get_find(s,lst)
if result==True:
    print('存在')
else:
    print('不存在')