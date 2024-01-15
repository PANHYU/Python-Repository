import re
pattern='黑客|破解|反爬'
s='我想学习python，想破解一些VIP视频，python可以实现无底线反爬吗？'
new_s=re.sub(pattern,'XXX',s)
print(new_s)

s2='https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1'
pattern2='[?|&]'
lst=re.split(pattern2,s2)
print(lst)