import pygame
import os


WIN_WIDTH = 400
WIN_HEIGHT = 600

IMG_FOLDER = "./imgs/"

PIPE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join(IMG_FOLDER,"pipe.png")))

#BASE_IMG = scale2x(img_load(os.path.join(IMG_FOLDER, "base.png")))
BASE_IMG = pygame.transform.scale(pygame.image.load(os.path.join(IMG_FOLDER, "base.png")), (WIN_WIDTH, WIN_HEIGHT))

#BG_IMG = scale2x(img_load(os.path.join(IMG_FOLDER, "bg.png")))
BG_IMG = pygame.transform.scale(pygame.image.load(os.path.join(IMG_FOLDER, "bg.png")), (WIN_WIDTH, WIN_HEIGHT))