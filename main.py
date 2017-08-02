# -*- coding: utf-8 -*
import pygame
from settings import Settings
from player import Player
import game_functions as gf
import blobs
def run_game():

    pygame.init()
    ai_settings = Settings()
    #创建屏幕
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Supreme Commander Kim VS Trump")
    #创建一艘飞船
    player = Player(screen)
     #创建n个blob
    my_blobs = blobs.Blobs()
    my_blobs.generate_blob(ai_settings, screen, player, ai_settings.blob_num_init)
    while True:
       
        #对各个事件做出反应
        gf.check_events(player, my_blobs, ai_settings)
        #更新屏幕
        if player.life_value > 0:
            gf.update_screen(ai_settings, screen, player, my_blobs)
        else:
            screen.fill([0,0,0])  
            pygame.display.flip()      

run_game()
