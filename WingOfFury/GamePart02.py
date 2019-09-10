
'''
Created on Aug 17, 2019

@author: kylin

需求一:
    1.加载 background.png创建背景
    2.将背景绘制在屏幕的(0,0)位置
    3.调用屏幕更新显示背景图像
需求二：
    1.加载hero1.png创建英雄飞机
    2.将英雄飞机绘制在屏幕的(200,500)的位置
    3.调用屏幕更新显示飞机图像
    
'''

import pygame

pygame.init()

#创建游戏的窗口
screen = pygame.display.set_mode(size=(480, 852))

#绘制背景图像
background = pygame.image.load("./image/background.png")
screen.blit(background, (0,0))
# pygame.display.update()


#绘制英雄的飞机
hero = pygame.image.load("./image/hero1.png")
screen.blit(hero, (200,500))
pygame.display.update()


while True:
    pass


pygame.quit()