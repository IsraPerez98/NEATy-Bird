import pygame
import neat
import time
import os
import random

import img
from bird import Bird

def draw_window(win,bird):
    win.blit(img.BG_IMG, (0,0))
    bird.draw(win)
    pygame.display.update()

def main():
    bird = Bird(200,200)
    win = pygame.display.set_mode((img.WIN_WIDTH,img.WIN_HEIGHT))
    clock = pygame.time.Clock()

    playing = True

    while playing:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False
        
        bird.move()
        draw_window(win,bird)

    pygame.quit()
    quit()

main()