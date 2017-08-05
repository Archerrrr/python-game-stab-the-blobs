# -*- coding: utf-8 -*

import sys
import pygame
import blobs

def check_events(player, blobs, settings):
    """相应各种按键、鼠标事件"""
    #为了根据事件修改玩家位置，需要玩家对象作为参数. 为了防止玩家位置超出屏幕范围，需要屏幕参数作为对象。
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player.moving_up = False
                player.moving_right = True
                player.moving_down = False
                player.moving_left = False
                if player.rect.right <= player.screen_rect.right - 2:
                    player.rect.centerx +=2
                    blobs.test_explode(player, settings)
            elif event.key == pygame.K_DOWN:
                player.moving_up = False
                player.moving_right = False
                player.moving_down = True
                player.moving_left = False
                if player.rect.bottom <= player.screen_rect.bottom - 2:
                    player.rect.centery +=2
                    blobs.test_explode(player, settings)
            elif event.key == pygame.K_LEFT:
                player.moving_up = False
                player.moving_right = False
                player.moving_down = False
                player.moving_left = True
                if player.rect.left >= 2:
                    player.rect.centerx -=2
                    blobs.test_explode(player, settings)
            elif event.key == pygame.K_UP:
                player.moving_up = True
                player.moving_right = False
                player.moving_down = False
                player.moving_left = False
                if player.rect.top >= 2:
                    player.rect.centery -=2
                    blobs.test_explode(player, settings)
                

                
            
            

def update_screen(settings, screen, player, blobs):
    """更新屏幕，并显示更新呢后的屏幕"""
    #参数依次是：游戏设置，屏幕，玩家形象
    screen.fill(settings.bg_color)
    #绘制飞船，注意要在填充背景之后进行。
    player.blitme()
    #绘制泡泡
    blobs.draw_blobs(screen)
    #让最近对屏幕的绘制可见
    pygame.display.flip()
