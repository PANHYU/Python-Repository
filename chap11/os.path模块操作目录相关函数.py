import os.path

#获取文件或目录的绝对路径
print(os.path.abspath('os模块.py'))

#判断文件或目录是否存在
print(os.path.exists('a.txt'),os.path.exists('demo1.py'))

#将目录与目录或者文件名拼接起来
print(os.path.join('E:\\Python','demo13.py'))

#将目录与文件拆分
print(os.path.split('E:\\vippython\\demo13.py'))

#分离文件名和扩展名
print(os.path.splitext('demo13.py'))

#从目录中提取文件名
print(os.path.basename('E:\\vippython\\demo13.py'))

#从一个路径中提取文件路径，不包括文件名
print(os.path.dirname('E:\\vippython\\demo13.py'))

#判断是否为路径
print(os.path.isdir('E:\\vippython\\demo13.py'))