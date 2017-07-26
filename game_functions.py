# -*- coding: utf-8 -*

import sys
import pygame

def check_events(player):
    """相应各种按键、鼠标事件"""
    #为了根据事件修改玩家位置，需要玩家对象作为参数
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player.rect.centerx +=2
            elif event.key == pygame.K_DOWN:
                player.rect.centery +=2
            elif event.key == pygame.K_LEFT:
                player.rect.centerx -=2
            elif event.key == pygame.K_UP:
                player.rect.centery -=2
                

                
            
            

def update_screen(settings, screen, player):
    """更新屏幕，并显示更新呢后的屏幕"""
    #参数依次是：游戏设置，屏幕，玩家形象
    screen.fill(settings.bg_color)
    #绘制飞船，注意要在填充背景之后进行。
    player.blitme()
    #让最近对屏幕的绘制可见
    pygame.display.flip()
