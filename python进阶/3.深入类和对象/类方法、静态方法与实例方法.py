'''
实例方法
静态方法
类方法
'''

class Date:
    def __init__(self,year,month,day):
        '''
        构造方法
        year:年
        month:月
        day:日
        '''
        self.year=year
        self.month=month
        self.day=day

    # 实例方法
    def __str__(self):
        return F'{self.year}/{self.month}/{self.day}'
    
    # 普通实例方法
    def tomorrow(self):
        self.day += 1
    
    # 静态方法
    @staticmethod
    def parse_from_string(date_str):
        year,month,day=date_str.split('-')
        #静态方法返回类的时候是写上当前的类名，硬编码，如果类名更改，那么返回的类名也必须保持一致
        return Date(int(year),int(month),int(day))
    
    # 类方法
    @classmethod
    def parse_string(cls,date_str):
        year,month,day=date_str.split('-')
        '''
        cls参数指向这个类
        类与实例对象不要混淆
        Date   类本身
        date=Date()  实例对象
        '''
        return cls(int(year),int(month),int(day))
    
    # 使用静态方法对当前日期进行校验
    @staticmethod
    def valid_str(date_str):
        year,month,day=date_str.split('-')
        if int(year)>0 and (int(month)>0 and int(month)<=12) and (int(day)>0 and int(day)<=31):
            return True
        else:
            return False
        


if __name__=='__main__':
    new_day=Date(2024,1,4)  # 当前这个类输出格式日期的时候，必须要传入三个参数
    print('当前日期：',new_day)
    new_day.tomorrow()
    print('明天的日期：',new_day)

# 如果现在想传入一个字符串，例如：2024-1-5
    # 普通做法
    date_str='2024-1-5'
    year,month,day=date_str.split('-')
    #print(year,month,day)
    new_day=Date(int(year),int(month),int(day))
    print(new_day)

    # 使用静态方法对字符串进行解析并格式化输出
    '''
    实例方法：
        必须使用实例对象.实例方法
    
    静态方法：
        类.类方法

    类方法：
        类.类方法

    类方法对于静态方法的区别在于需要传入一个参数cls, cls指向类本身
    '''

    new_day=Date.parse_from_string(date_str)
    print('静态方法字符串解析输出：',new_day)

    new_day=Date.parse_string(date_str)
    print('类方法字符串解析输出：',new_day)

    # 日期校验
    new_day=Date.valid_str('2024-1-33')
    print(new_day)