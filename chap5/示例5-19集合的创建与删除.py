#{}直接创建集合
s={10,20,30}
print(s)
#集合只能存储不可变数据类型
#s={[10,20],[30,40]} TypeError: unhashable type: 'list'
#print(s)

#使用set()创建集合
s=set() #创建一个空集合，空集合的布尔值为False
print(s)
s={} #创建的是字典
print(s,type(s))

s=set('helloworld')
print(s)

s2=set([10,20,30])
print(s2)

s3=set(range(1,10))
print(s3)

#集合属于序列的一种
print('max:',max(s3))
print('min:',min(s3))
print('len:',len(s3))

print('9在集合中存在吗？',(9 in s3))
print('9在集合中不存在吗？',(9 not in s3))

#集合的删除
del s3
#print(s3)