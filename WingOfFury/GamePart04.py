'''
Created on Aug 17, 2019

@author: kylin

步骤一：
    1.新建plane_sprites.py文件
    2.定义GameSprite继承自pygame.sprite.Sprite
    注意：如果一个类的父类不是object，在重写初始化方法时，一定要先super()一下父类的__init__()方法
需求：
    使用刚刚派生的游戏精灵和精灵组创建敌机并实现敌机动画
'''
import pygame
from plane_sprites import *

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

#创建时钟对象
clock =pygame.time.Clock()

#定义rect记录飞机的初始位置
hero_rect = pygame.Rect(200,500,100,124)



#创建敌机的精灵
emeny = GameSprite("./image/enemy0.png")
emeny1 = GameSprite("./image/enemy0.png", 2)


#创建敌机的精灵组
emeny_group = pygame.sprite.Group(emeny,emeny1)



while True: 
    clock.tick(60)

    #设置点击关闭按钮后退出游戏
    #监听事件
    for event in pygame.event.get():
        #判断事件类型是否是退出事件
        if event.type == pygame.QUIT:
            print("游戏退出。。。")
            # quit 卸载所有模块
            pygame.quit()
            # exit()退出系统 直接终止当前正在执行的程序
            exit()
    
    hero_rect.y -= 1
    
    #判断飞机的位置
    if hero_rect.y <= -124:
        hero_rect.y = 852
    
    screen.blit(background,(0,0))
    screen.blit(hero, hero_rect)
    
    #让精灵组调用两个方法
    emeny_group.update()
    emeny_group.draw(screen)
    
    
    pygame.display.update()   
    
pygame.quit()