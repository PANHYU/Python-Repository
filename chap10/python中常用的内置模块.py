import sys
import time
import urllib.request

print(sys.getsizeof(25))
print(sys.getsizeof(88))
print(sys.getsizeof(True))
print(sys.getsizeof(False))
print('-'*40)
print(time.time())
print(time.localtime(time.time()))
print('-'*40)
print(urllib.request.urlopen('http://www.baidu.com').read())