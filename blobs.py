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
    
    def test_explode(self, player):
        for value in range(0,len(self.blob_list)):
                if ((self.blob_list[value].x - player.rect.centerx)**2 + (self.blob_list[value].y - player.rect.centery)**2 < (self.blob_list[value].radius)**2 ) and (self.blob_list[value].will_explode == 0):
                    self.blob_list[value].color = [255,0,0]
                    self.blob_list[value].will_explode = 1
                    self.timer = threading.Timer(3, self.exclude_blob, [self.blob_list[value].id])
                    self.timer.start()
    def exclude_blob(self, id):
        for value in range(0,len(self.blob_list)):
            if self.blob_list[value].id == id:
                self.blob_list.pop(value)
                break
