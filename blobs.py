# -*- coding: utf-8 -*

import random
import pygame
import threading

class Blob():
    def __init__(self,settings, screen, player, id):
        while(1):
            self.radius = random.randint(settings.blob_size_bottom, settings.blob_size_top)
            self.x = random.randint(self.radius, screen.get_rect().right - self.radius)
            self.y = random.randint(self.radius, screen.get_rect().bottom - self.radius)
            self.color = [0,0,255]
            self.will_explode = 0
            self.id = id
            if (self.x - player.rect.centerx)**2 + (self.y - player.rect.centery)**2 > (player.rect.width / 2)**2 :
                break
        
        
class Blobs():
    def __init__(self):
        self.blob_list = []
                
    def generate_blob(self, settings, screen, player, n):
        num_blobs = 0
        while(num_blobs<n):
            self.new_blob = Blob(settings, screen, player, num_blobs)
            self.blob_list.append(self.new_blob)
            num_blobs = num_blobs + 1
            
    def draw_blobs(self,screen):
        for blob in self.blob_list:
            pygame.draw.circle(screen,blob.color,[blob.x,blob.y],blob.radius,1)
    
    def test_explode(self, player, settings):
        for value in range(0,len(self.blob_list)):
                if ((self.blob_list[value].x - player.rect.centerx)**2 + (self.blob_list[value].y - player.rect.centery)**2 < (self.blob_list[value].radius)**2 ) and (self.blob_list[value].will_explode == 0):
                    self.blob_list[value].color = [255,0,0]
                    self.blob_list[value].will_explode = 1
                    self.blob_list[value].radius = self.blob_list[value].radius * 2
                    self.timer = threading.Timer(settings.blob_explode_time, self.exclude_blob, [self.blob_list[value].id, player, settings])
                    self.timer.start()
    def exclude_blob(self, id, player, settings):
        for value in range(0,len(self.blob_list)):
            if self.blob_list[value].id == id:
                distdist = (self.blob_list[value].x - player.rect.centerx)**2 + (self.blob_list[value].y - player.rect.centery)**2
                if distdist == 0:
                    player.life_value = 0
                elif ( distdist < ((self.blob_list[value].radius)**2)  ):
                    player.punish(  ((self.blob_list[value].radius)**2)/distdist*10  )
                #注意，左右工作结束后才能删除这个泡泡，因为删除操作将导致列表index变化
                temp_blob = self.blob_list.pop(value)
                
                #对这个泡泡的临近泡泡，也让其进入即将爆炸状态。
                for value_inner in range(0,len(self.blob_list)):
                    if value_inner >= len(self.blob_list):
                        break
                    #如果这个泡泡已经进入爆炸状态了，就不用管了
                    elif self.blob_list[value_inner].will_explode == 1:
                        continue
                    else:
                        distdist_inner = (temp_blob.x - self.blob_list[value_inner].x)**2 + (temp_blob.y - self.blob_list[value_inner].y)**2
                        if distdist_inner < (self.blob_list[value_inner].radius + temp_blob.radius)**2:
                            self.blob_list[value_inner].color = [255,0,0]
                            self.blob_list[value_inner].will_explode = 1
                            self.blob_list[value_inner].radius = self.blob_list[value_inner].radius * 2
                            self.timer = threading.Timer(settings.blob_explode_time,self.exclude_blob,[self.blob_list[value_inner].id, player, settings])
                            self.timer.start()

                break
