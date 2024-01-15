class Instrument(): #父类
    
    def make_sound(self):
        pass

class Erhu(Instrument):
    def make_sound(self):
        print('二胡在弹奏')

class Piano(Instrument):
    def make_sound(self):
        print('钢琴在弹奏')

class Violin(Instrument):
    def make_sound(self):
        print('小提琴在弹奏')

#编写一个函数
def play(obj):
    obj.make_sound()

#测试
er=Erhu()
piano=Piano()
vio=Violin()

#调用方法
play(er)
play(piano)
play(vio)
#或者
#er.make_sound()
#piano.make_sound()
#vio.make_sound()