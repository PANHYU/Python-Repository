class Date:
    def __init__(self,year,month,day):
        self.year=year
        self.month=month
        self.day=day

    def __str__(self):
        return F'{self.year}/{self.month}/{self.day}'

    def tomorrow(self):
        self.day += 1

    @staticmethod
    def parse_from_string(date_str):
        year,month,day=date_str.split('-')
        return Date(int(year),int(month),int(day))

    @classmethod
    def parse_string(cls,date_str):
        year,month,day=date_str.split('-')
        return cls(int(year),int(month),int(day))
    
class User:
    #私有属性
    '''
    私有属性无法被实例对象直接获取
    在继承关系中，子类也无法直接获取到私有属性
    '''
    def __init__(self,birthday):
        #self.birthday=birthday
        self.__birthday=birthday
    
    #私有属性只能被当前这个类中的方法直接获取
    def age_get(self):
        return 2024-self.__birthday.year
    
if __name__=='__main__':
    user=User(Date(1990,11,20))
    print(user._User__birthday)
    print('年龄为：',user.age_get())

'''
在python中，私有属性其实是python在执行的过程中对私有属性的名称进行了重命名
    _类名.__属性名称

这个私有属性只是相对安全
私有属性的命名方式只是让开发者知道当前的这个变量是一个私有数据而已
'''
