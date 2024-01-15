import re
pattern='\d\.\d+'
s='I study Python3.11 every day Python2.7 I like you'
match=re.search(pattern,s)
print(match)
s2='I study Python every day'
match2=re.search(pattern,s2)
print(match2) #None
print(match.group())