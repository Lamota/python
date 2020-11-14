import random
import pygame
PRAME_PER_SEC = 60
SCREEN_RECT = pygame.Rect(0,0,480,700)
CREATE_ENEMY_EVENT = pygame.USEREVENT
HERO_FIRE_EVENT = pygame.USEREVENT + 1
class GameSprite(pygame.sprite.Sprite):
    """飞机大战游戏精灵"""

    def __init__(self, image_name, speed=1):

        # 调用父类的初始化方法
        super().__init__()

        # 定义对象的属性
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):

        # 在屏幕的垂直方向上移动
        self.rect.y += self.speed

class Back_ground(GameSprite):
     def __init__(self,is_alt = False):
         super().__init__("./images/background.png")
         if is_alt:
             self.rect.y = -self.rect.height
     def update(self):
         super().update()
         if self.rect.y >= SCREEN_RECT.height:
             self.rect.y = -SCREEN_RECT.height

class Enemy(GameSprite):
    def __init__(self):
        super().__init__("./images/enemy1.png")
        self.speed = random.randint(2,4)
        #y方向初始
        self.rect.bottom = 0
        #x初始
        max_x = SCREEN_RECT.width-self.rect.width
        self.rect.x = random.randint(0,max_x)
    def update(self):
        super().update()
        #判断是否飞出屏幕
        if self.rect.y >= SCREEN_RECT.height:
            print("敌机飞出屏幕...")
            self.kill()
    #判断对象是否被销毁
    def __del__(self):
        print("敌机销毁 %s" %self.rect)

class Hero(GameSprite):
    def __init__(self):
        super().__init__("./images/me1.png",0)
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom-120
        self.bullets = pygame.sprite.Group()
    def update(self):
        self.rect.x += self.speed
        #控制英雄不能离开屏幕
        if self.rect.x < 0:
            self.rect.x = 0

        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right
    def fire(self):
      for i in (0,1,2):
        bullet = Bullet()
        bullet.rect.bottom = self.rect.y - i*20
        bullet.rect.centerx = self.rect.centerx
        self.bullets.add(bullet)
        print("发射子弹")
class Bullet(GameSprite):
    def __init__(self):
        super().__init__("./images/bullet1.png",-2)
    def update(self):
        super().update()
        if self.rect.bottom < 0:
            self.kill()
        pass
    def __del__(self):
        print("子弹被销毁")


