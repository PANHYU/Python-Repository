import re
pattern='\d\.\d+'
s='I study Python3.11 every day Python2.7 I like you'
s2='3.8 Python I study every day'
s3='I study Python every day'
lst=re.findall(pattern,s)
lst2=re.findall(pattern,s2)
lst3=re.findall(pattern,s3)
print(lst)
print(lst2)
print(lst3)