'''
Created on Aug 17, 2019

@author: kylin
需求：
    1.在游戏初始化定义一个pygame.Rect的变量记录英雄的初始位置
    2.在游戏循环中每次让英雄的 y-1 ————向上移动
    3.y<=0将英雄移动到屏幕的底部
注意：每一次调用update()方法之前，需要把所有的游戏图像都重新绘制一遍，而且应该最先重新绘制背景图像
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

#创建时钟对象
clock =pygame.time.Clock()

#定义rect记录飞机的初始位置
hero_rect = pygame.Rect(200,500,100,124)

#测试tick函数
#i = 0

while True:
    #clock.tick(1)
    #i += 1
    #print(i)
    
    # 以下代码运行后会产生飞机残影，去除残影的方法就是重新绘制背景图像。
    """
    clock.tick(1)
    hero_rect.y -=50
    screen.blit(hero, hero_rect)
    pygame.display.update()
    """
    
    clock.tick(60)
    
    #捕获事件
    """
    event_list = pygame.event.get()
    if len(event_list) > 0:
        print(event_list)
    """
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
    pygame.display.update()   
    
pygame.quit()