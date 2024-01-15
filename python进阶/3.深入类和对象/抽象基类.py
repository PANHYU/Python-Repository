'''
什么是抽象基类
    java
        面向对象语言
        不支持多继承
        
        特殊的类：抽象类
            1.不能被实例化
            2.可以继承
            3.继承抽象类之后必须重载（重写）抽象类方法
'''

'''
python 抽象类的概念
    可以把抽象基类想象成一个创建实例对象的模板，
    但是在使用这个模板的时候必须要重载这个模板中所实现的方法
    并且这个模板不能自己实例化，必须借助于继承
    继承抽象类之后，必须进行抽象类方法重写

抽象基类可用于: 1.类型判断  2.对于类进行方法的限制
'''

class Company:
    def __init__(self,employee_list):
        self.employee=employee_list

    def __len__(self):
        return len(self.employee)
    
com=Company(['java','python'])
print(hasattr(com,'__len__'))  #要求程序员知道当前这个类中实现了__len__

#类型判断
from collections.abc import Sized
print(isinstance(com,Sized))

#抽象基类不能实例化
#s=Sized()

#继承抽象基类必须重载内部方法
# class Test(Sized):
#     def __len__(self):
#         pass

# test=Test()


'''
场景二
我们在去实现某个类的时候，必须要实现指定的类方法
框架中见的比较多

web框架  django
django框架中实现了缓存功能(组件)
redis
cache
memorycache

方法调用的统一
    因为现在不确定用户使用的是redis缓存，还是文件缓存
    redis设置缓存 和 文件设置缓存 不一样
    因此必须要让用户自己手动实现
'''

# class CacheBase:
#     def get(self,key):
#         raise NotImplementedError
    
#     def set(self,key,value):
#         raise NotImplementedError
    
# class RedisCache(CacheBase):
#     #如果用户没有重写set和get方法的时候，抛出异常
#     pass

# redis_cache=RedisCache()
# redis_cache.set('name','Java')


#导入python全局的抽象基类
import abc

#限制使用者必须按照规则使用内置的接口 api
class CacheBase(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get(self,key):
        pass

    @abc.abstractmethod
    def set(self,key,value):
        pass

class RedisCache(CacheBase):
    def get(self,key):
        pass
    
    def set(self,key,value):
        pass

redis_cache=RedisCache()
