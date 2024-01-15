import os
print(os.getcwd()) #返回当前的工作目录

#返回指定路径下的文件和目录信息
lst=os.listdir('chap11') #如果需要返回上一级就在文件名之前加../
print(lst)

#创建目录
#os.mkdir('newdir')

#创建多级目录
#os.makedirs('A/B/C')

#删除目录
#os.rmdir('newdir')

#删除多级目录
#os.removedirs('A/B/C')

#将path设置为当前工作目录
#os.chdir('')  #引号内加入需要修改为的path