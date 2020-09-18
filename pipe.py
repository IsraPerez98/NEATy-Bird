import pygame
import os
import random

import img

PIPE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join(img.IMG_FOLDER,"pipe.png")))

class Pipe:
    VERTICAL_GAP = 200 # the vertical gap between the top and bottom pipes
    VEL = 5

    def __init__(self,x):
        self.x = x
        self.height = 0

        self.height_top = 0
        self.height_bottom = 0
        
        self.PIPE_TOP_IMG = pygame.transform.flip(PIPE_IMG, False, True)
        self.PIPE_BOTTOM_IMG = PIPE_IMG

        self.completed = False
        self.set_height()

    def set_height(self):
        self.height = random.randrange(80, img.WIN_HEIGHT -  350)
        self.height_top = self.height - self.PIPE_TOP_IMG.get_height()
        self.height_bottom = self.height + self.VERTICAL_GAP

    def move(self):
        self.x -= self.VEL
    
    def draw(self, win):
        win.blit(self.PIPE_TOP_IMG, (self.x, self.height_top))
        win.blit(self.PIPE_BOTTOM_IMG, (self.x, self.height_bottom))

    def collide(self, bird):
        bird_mask = bird.get_mask()
        top_mask = pygame.mask.from_surface(self.PIPE_TOP_IMG)
        bottom_mask = pygame.mask.from_surface(self.PIPE_BOTTOM_IMG)

        top_offset = (self.x - bird.x, self.height_top - round(bird.y))
        bottom_offset = (self.x - bird.x, self.height_bottom - round(bird.y))

        bottom_collide_point = bird_mask.overlap(bottom_mask, bottom_offset)
        top_collide_point = bird_mask.overlap(top_mask, top_offset)

        if (bottom_collide_point or top_collide_point):
            return True
        
        return False
    
