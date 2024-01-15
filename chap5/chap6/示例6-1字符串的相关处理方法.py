#大小写转换
s1='HelloWorld'
s2=s1.lower()
s3=s1.upper()
print(s1,s2,s3)

#字符串的分隔
mail='devipan@126.com'
lst=mail.split('@')
print(lst)
print('邮箱名：',lst[0],'邮件服务器域名：',lst[1])

print(s1.count('o')) # o在s1中出现了两次

#检索操作
print(s1.find('o')) # o在字符串s1中首次出现的位置
print(s1.find('p')) # -1,表示没有找到

print(s1.index('o')) 
#print(s1.index('p')) #ValueError: substring not found 子串没有找到

#判断前缀和后缀
print(s1.startswith('H'))
print(s1.startswith('P'))

print('demo.py'.endswith('.py'))
print('text.txt'.endswith('.txt'))