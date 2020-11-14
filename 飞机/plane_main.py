import pygame
from plane_sprites import *
class PlaneGame(object):
    def __init__(self):
        print("游戏初始化")
        #游戏窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        #游戏时钟
        self.clock = pygame.time.Clock()
        #调用私有方法
        self.__creat_sprites()
        pygame.time.set_timer(CREATE_ENEMY_EVENT,1000)
        pygame.time.set_timer(HERO_FIRE_EVENT,500)
    def __creat_sprites(self):
        bg1 = Back_ground()
        bg2 = Back_ground(True)
        self.back_group = pygame.sprite.Group(bg1,bg2)
        #创建敌机精灵组
        self.enemy_Group = pygame.sprite.Group()
        self.hero = Hero()
        self.hero_Group = pygame.sprite.Group(self.hero)


    def start_game(self):
        print("游戏开始...")
        while True:
            # 设置刷新频率
            self.clock.tick(PRAME_PER_SEC)
            # 事件监听
            # 碰撞检测
            # 更新绘制精灵组
            # 更新显示
            self.__event_handler()
            self.__check_collide()
            self.__update_sprites()
            pygame.display.update()
    def __event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return self.__game_over()
            elif event.type == CREATE_ENEMY_EVENT:
                print("敌机出场")
                enemy = Enemy()
        #将敌机精灵添加到精灵组
                self.enemy_Group.add(enemy)
            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()
        # 使用键盘提供的方法获取键盘按键 - 按键元组
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_RIGHT]:
            self.hero.speed = 3
        elif keys_pressed[pygame.K_LEFT]:
            self.hero.speed = -3
        else:
            self.hero.speed = 0

            print("向右移动")

    def __check_collide(self):
        pygame.sprite.groupcollide(self.hero.bullets,self.enemy_Group,True,True)
        enemies = pygame.sprite.spritecollide(self.hero,self.enemy_Group,True)
        if len(enemies) > 0:
            self.hero.kill()
            PlaneGame.__game_over()



    def __update_sprites(self):
        self.back_group.update()
        self.back_group.draw(self.screen)

        self.enemy_Group.update()
        self.enemy_Group.draw(self.screen)

        self.hero_Group.update()
        self.hero_Group.draw(self.screen)

        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)




    @staticmethod
    def __game_over():
        print("游戏结束")
        pygame.quit()
        exit()

if __name__ == '__main__':
    game = PlaneGame()
    game.start_game()
