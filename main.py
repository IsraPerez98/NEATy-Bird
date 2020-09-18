import pygame
import neat
import time
import os

import img
from bird import Bird
from base import Base
from pipe import Pipe

def draw_window(win,bird, pipes, base):
    win.blit(img.BG_IMG, (0,0))
    
    for pipe in pipes:
        pipe.draw(win)
    
    base.draw(win)
    
    bird.draw(win)
    pygame.display.update()

def main():
    bird = Bird(230,350)
    base = Base(img.WIN_HEIGHT - 70)
    pipes = [Pipe(700)]
    win = pygame.display.set_mode((img.WIN_WIDTH,img.WIN_HEIGHT))
    clock = pygame.time.Clock()

    playing = True

    while playing:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False
        
        bird.move()
        draw_window(win,bird,pipes,base)

    pygame.quit()
    quit()

main()