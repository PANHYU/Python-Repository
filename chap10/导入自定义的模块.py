#导入clac自定义模块使用
import calc
print(calc.add(20,30))
print(calc.div(20,5))

print('-'*40)
from calc import add
print(add(20,30))