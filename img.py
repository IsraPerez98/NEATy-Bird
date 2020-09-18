import pygame
import os


WIN_WIDTH = 500
WIN_HEIGHT = 650

IMG_FOLDER = "./imgs/"

#BASE_IMG = scale2x(img_load(os.path.join(IMG_FOLDER, "base.png")))

#BG_IMG = scale2x(img_load(os.path.join(IMG_FOLDER, "bg.png")))
BG_IMG = pygame.transform.scale(pygame.image.load(os.path.join(IMG_FOLDER, "bg.png")), (WIN_WIDTH, WIN_HEIGHT))