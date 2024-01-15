'''
多态
    继承：多态一定是发生在子类和父类之间的
    重写：子类重写父类中的方法

面向对象语言中实现多态的通用方法
'''

# class Animal:
#     def say(self):
#         print('I am an animal')

# class Cat(Animal):
#     def say(self):
#         print('I am a cat')

# class Dog(Animal):
#     def say(self):
#         print('I am a dog')

# class Duck(Animal):
#     def say(self):
#         print('I am a duck')

# duck=Duck()
# duck.say()

# dog=Dog()
# dog.say()

'''
鸭子类型
    一种动物长得像鸭子，叫起来也像鸭子，那么这个动物就是一个鸭子
    多个类中实现了同一个方法(当前的方法名称一样)
    不关注方法的实现方式，只关注当前这个方法的名称

Python的关注点是当前这个对象的类型
'''
class Cat:
    def say(self):
        print('I am a cat')

class Dog:
    def say(self):
        print('I am a dog')

class Duck:
    def say(self):
        print('I am a duck')

animal=Cat
animal().say()

animal=Dog
animal().say()

animal_list=[Cat,Dog,Duck]
for animal in animal_list:
    animal().say()


#关于鸭子类型的实现案例
list_a=[1,2]
list_b=[3,4]

list_a.extend(list_b)
print(list_a)

set_data=set()
set_data.add(5)
set_data.add(6)

list_a.extend(set_data)
print(list_a)

#list_a 是一个列表类型，为什么集合也可以进行追加
'''
extend -> 只要是迭代类型，就可以进行追加
list,set 都是可迭代的
__iter__
根据鸭子类型，list和set都实现了__iter__方法，因此list和set都可以归为可迭代的类
'''