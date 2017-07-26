# -*- coding: utf-8 -*

import pygame

class Player():
    #包含的成员变量：屏幕(内含其矩形），player外观，player矩形，当前移动方向。外观的矩形内含有位置属性
    def __init__(self, screen):
        """初始化玩家扮演的人物，并设置其初始位置。"""
        self.screen = screen
        
        #加载玩家扮演的人物的形象
        self.image = pygame.image.load('./player.bmp')
        
        #获取形象的rect属性
        self.rect = self.image.get_rect()
        #获取屏幕的rect属性
        self.screen_rect = screen.get_rect()
        
        #把玩家初始位置设置为屏幕的中心
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        
        
    def blitme(self):
        """把图像image根据其rect属性绘制到屏幕的相应位置。"""
        #调用的是player对象的screen属性的方法，为什么能修改屏幕的属性？已知传参在参数可变的情况下实际传递的是参数的引用，那么复制操作实际也是引用吗？"""
        self.screen.blit(self.image, self.rect)
        

            
            
