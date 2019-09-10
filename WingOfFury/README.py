'''
Created on Aug 17, 2019

@author: kylin
'''
'''
游戏的第一印象
    把一些静止的图像绘制到游戏窗口中
    根据用户的交互或者其他情况，移动这些图像，产生动画效果
    根据图像之间是否发生重叠，判断敌机是否被摧毁等其他情况

01 使用pygame创建图形窗口
    1. 游戏的初始化和退出
        pygame.init() -> 游戏代码 -> pygame.quit()
    2. 理解游戏中的坐标系
        原点在左上角；x轴水平向右；y轴垂直向下
        在游戏中，所有可见元素 都是以矩形区域来描述
            描述一个矩形区域有四个要素(x,y)(width,height)
        pygame中用来描述矩形区域的类 pygame.Rect 
            Rect(x,y,width,height）-> Rect
        Rect中的bottom属性是 图像顶部的y值加上图像高度，将bottom设置为0 就等于将y属性设置为图像高度负值
    3. 创建游戏主窗口
        pygame提供了一个模块pygame.display来用于创建、管理游戏窗口
            set_mode方法 用于初始化游戏显示窗口
                set_mode(resolution = (0,0), flags = 0, depth = 0) -> Surface
                    resolution:指定屏幕的宽和高，默认创建窗口大小和屏幕大小一致
                    flags:参数指定屏幕的附加选项
                    depth:参数表示颜色的位数，默认自动匹配
    4. 简单的游戏循环
        while True:
    
02 理解图像并实现图像绘制
    在屏幕上看到某一个图像的内容，需要以下三个步骤：
        1.使用pygame.image.load()加载图像数据
        2.使用游戏屏幕对象，调用blit方法将图像绘制到指定位置
        3.调用pygame.display.update()方法更新整个屏幕的显示
    在所有的blit之后统一调用一次update方法

03 理解游戏循环和游戏时钟
    游戏循环意味着游戏的正式开始
    游戏的初始化：设置游戏窗口->绘制图像初始位置->设置游戏时钟
    游戏循环：设置刷新帧率->检测用户交互->更新所有图像位置->更新屏幕显示
        pygame中提供了一个类 pygame.time.Clock 可以设置屏幕绘制速度——刷新帧率
    游戏时钟
        使用时钟对象的步骤：
            1）在游戏初始化创建一个时钟对象 
            2）在游戏循环中让时钟对象调用tick方法，tick方法根据上次被调用的时间，自动设置游戏循环的延时
                clock.tick(n) 每秒变换n次
    在游戏循环中监听事件
        事件 event： 是游戏启动后，用户针对游戏所做的操作，如点击关闭按钮，点击鼠标等
        监听：在游戏循环中，判断用户具体的操作
        代码实现：
            pygame中通过pygame.event.get()可以获得用户当前所作动作的事件列表

04 理解精灵和精灵组
    pygame.sprite.Sprite ——————储存图像数据image和位置rect的对象
        精灵类提供 update()方法用于更新精灵位置
    pygame.sprite.Group
        精灵组提供的方法：
            __init__(self,*精灵):
            add(*sprites):向组中增加精灵
            sprite():返回所有精灵列表
            update(*args):让组中的所以精灵调用update方法
            draw(Surface):将组中所有精灵的image，绘制到Surface的rect位置
    游戏初始化：创建精灵 -> 创建精灵组
    游戏循环：精灵组.update() -> 精灵组.draw(screen) -> pygame.display.update()
    
05 明确飞机游戏中类的设计
    PlaneGame：
        属性：
            screen
            clock
            精灵组或精灵
        方法：
            __init__()
            __create_sprites()
            start_game()
            __event_handler()
            __check_collide()
            __update_sprites()
            __game_over()
    
    游戏初始化：设置游戏窗口 -> 创建游戏时钟 -> 创建精灵组，精灵
    游戏循环： 设置刷新频率 -> 事件监听 -> 碰撞检测 -> 更新/绘制精灵组 ->更新屏幕显示
    
    定时器：在pygame中可以用pygame.time.set_timer()来添加定时器
        set_timer(eventid,milliseconds) -> None
            第一个参数是事件代号，基于pygame.USEREVENT来指定
            第二个参数是事件触发间隔的毫秒值
        set_timer可以创建一个事件，可以在游戏循环的事件监听中被捕获
        监听判断event.type是否等于eventid，如果相等，表示定时器事件发生
            步骤:
                1. 定义 定时器常量----eventid
                2. 在初始化方法中，调用set_timer方法设置定时器事件
                3. 在游戏循环中，监听定时器事件
        
    捕获按键：
        方法一： 判断event.type == pygame.KEYDOWN
                （用户如果要再次触发事件，需要抬起手指重新按键）
        方法二： 首先使用 pygame.key.get_pressed() 返回所有按键的元组
                通过键盘常量，判断元组中某一个键是否被按下----如果被按下，对应的数值为1
                (用户可以按下某个键不放，持续捕获)
                
    碰撞检测 
    pygame.sprite.groupcollide():两个精灵组中所有的精灵的碰撞检测
        groupcollide(group1,group2,dokill1,dokill2,collided = None) -> Sprite_dict
            如果将dokill设置为True 则发生碰撞的精灵将被自动移除
            collided 参数是用于计算碰撞的回调函数 如果没有指定，则每个精灵必须有rect属性
    pygame.sprite.spritecollide():某个精灵和指定精灵组中的精灵的碰撞
        spritecollide(sprite,group,dokill,collided = None) -> Sprite_list
            如果将dokill设置为True，则指定精灵组中发生碰撞的精灵将被自动移除
    
                
定义一个GameSprite类
    属性：
        image 精灵图像 使用image_name加载
        rect 精灵大小 默认使用图像大小
        speed 精灵移动速度 默认为1
    方法：
        update 精灵更新 让精灵的self.rect.y += self.speed

定义一个背景类
    思路：
        1.创建两张背景图像精灵
            第一张完全和屏幕重合
            第二张在屏幕的正上方
        2.两张图像一起向下方运动
            self.rect.y += self.speed
        3.当任意背景精灵的 rect.y >= 屏幕的高度 说明已经移动到屏幕下方
        4.将移动到屏幕下方的这张图像设置到屏幕的正上方
            rect.y = -rect.height
            

定义一个Enemy子类
    需求：
        1.游戏启动后，每隔一秒会出现一架敌机
        2.每架敌机向屏幕下方飞行，飞行速度各不相同
        3.每架敌机出现的水平位置也不尽相同
        4.当敌机从屏幕下方飞出，不会再飞回到屏幕中

定义一个英雄类
    需求：
        1.游戏启动后，英雄出现在屏幕的水平中间位置，距离屏幕底部120像素
        2.英雄每隔0.5秒发射一次子弹，每次连发三枚子弹
        3.英雄默认不会移动，需要通过左/右方向键，控制英雄在水平方向移动

定义一个子弹类
    需求：
        1.子弹从英雄的正上方发射，沿直线向上方飞行
        2.飞出屏幕后，需要从精灵组中删除
        
    
'''