class Car():
    def __init__(self,type,no):
        self.type=type
        self.no=no
    
    def start(self):
        print('我是车，我能启动')
    def stop(self):
        print('我是车，我可以停止')

#出租车
class Taxi(Car):
    def __init__(self, type, no,company):
        super().__init__(type, no)
        self.company=company
    
    # 重写父类的启动和停止方法
    def start(self):
        print('乘客您好！')
        print(f'我是{self.company}出租车公司，我的车牌是：{self.no},您要去哪里？')
    
    def stop(self):
        print('目的地到了，请您扫码付款，欢迎下次乘坐')

#家用轿车
class FamilyCar(Car):
    def __init__(self, type, no,name):
        super().__init__(type, no,)
        self.name=name

    def start(self):
        print(f'我是{self.name},我的轿车我做主')

    def stop(self):
        print('目的地到了，我们去玩吧！')
    
#测试
taxi=Taxi('出租车','1001','长城')
fam=FamilyCar('家用轿车','1002','武大郎')
taxi.start()
taxi.stop()
print('-'*40)
fam.start()
fam.stop()
