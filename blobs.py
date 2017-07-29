import random
import pygame

class Blob():
    def __init__(self,settings, screen, player):
        while(1):
            self.radius = random.randint(settings.blob_size_bottom, settings.blob_size_top)
            self.x = random.randint(self.radius, screen.get_rect().right - self.radius)
            self.y = random.randint(self.radius, screen.get_rect().bottom - self.radius)
            if (self.x - player.rect.centerx)**2 + (self.y - player.rect.centery)**2 > (player.rect.width / 2)**2 :
                break
                
        
class Blobs():
    def __init__(self):
        self.blob_list = []
        
    def generate_blob(self, settings, screen, player, n):
        while(len(self.blob_list)<n):
            self.new_blob = Blob(settings, screen, player)
            self.blob_list.append(self.new_blob)
    
    def draw_blobs(self,screen):
        for blob in self.blob_list:
            pygame.draw.circle(screen,[255,0,0],[blob.x,blob.y],blob.radius,1)
    
