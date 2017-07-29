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
    my_blobs.generate_blob(ai_settings, screen, player, 5)
    while True:
       
        #对各个事件做出反应
        gf.check_events(player)
        #更新屏幕
        gf.update_screen(ai_settings, screen, player, my_blobs)
        

run_game()
