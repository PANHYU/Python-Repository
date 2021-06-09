#coding:gbk
"""
第一个小项目：Rock-paper-scissors-lizard-Spock
作者：潘皖
日期：2021/6/2
"""
import random
def name_to_number(name):
	if name == "石头":
		return 0
	elif name == "史波克":
		return 1
	elif name == "纸":
		return 2
	elif name == "蜥蜴":
		return 3
	elif name == "剪刀":
		return 4
	else:
		print("Error: No Correct Name")
 
def number_to_name(number):
	if number in range(0,5):
		if number == 0:
			return "石头"
		elif number == 1:
			return "史波克"
		elif number == 2:
			return "纸"
		elif number == 3:
			return "蜥蜴"
		elif number == 4:
			return "剪刀"
	
 
def rpsls(player_choice):
    print("您的选择为:",player_choice)
    player_number = name_to_number(player_choice)
    comp_number = random.randrange(0,5)
    comp_choice = number_to_name(comp_number)
    print("计算机的选择为:",comp_choice)
    if player_number - comp_number in range(-4,-2) or player_number - comp_number in range(1,3):
        print("您赢了！")
    elif player_number - comp_number in range(-2,0) or player_number - comp_number in range(3,5):
        print("机器赢了")
    elif player_number - comp_number == 0:
        print("平局")
    
print("欢迎使用RPSLS游戏")
print("----------------")
print("请输入您的选择:")
player_choice=input()
rpsls(player_choice)
