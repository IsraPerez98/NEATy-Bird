import pygame
import os

import img

BIRD_IMAGES = [ pygame.transform.scale2x(pygame.image.load(os.path.join(img.IMG_FOLDER,"bird1.png"))),
                pygame.transform.scale2x(pygame.image.load(os.path.join(img.IMG_FOLDER,"bird2.png"))),
                pygame.transform.scale2x(pygame.image.load(os.path.join(img.IMG_FOLDER,"bird3.png"))),
]

class Bird: 
    IMGS = BIRD_IMAGES
    MAX_ROTATION = 25
    ROT_VEL = 20
    ANIMATION_TIME = 5
    TERMINAL_VELOCITY = 16

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tilt = 0
        self.tick_count = 0
        self.vel = 0
        self.height = self.y
        self.img_count = 0
        self.img = self.IMGS[0]

    def jump(self):
        self.vel = -10.5
        self.tick_count = 0
        self.height = self.y
    
    def calcTilt(self, displacement):
        if displacement < 0 or self.y < self.height + 50:
            if self.tilt < self.MAX_ROTATION:
                self.tilt = self.MAX_ROTATION
        else:
            if self.tilt > -90:
                self.tilt -= self.ROT_VEL

    def move(self):
        self.tick_count += 1

        displacement = self.vel * self.tick_count + 1.5 * self.tick_count ** 2

        if displacement >= self.TERMINAL_VELOCITY:
            displacement = self.TERMINAL_VELOCITY
        
        if displacement <= 0:
            displacement -= 2 #makes the animation better

        self.y += displacement

        self.calcTilt(displacement)
    
    def draw(self, win):
        self.img_count += 1

        if self.img_count < self.ANIMATION_TIME:
            self.img = self.IMGS[0]
        elif self.img_count < self.ANIMATION_TIME * 2:
            self.img = self.IMGS[1]
        elif self.img_count < self.ANIMATION_TIME * 3:
            self.img = self.IMGS[2]
        elif self.img_count < self.ANIMATION_TIME * 4:
            self.img = self.IMGS[1]
        elif self.img_count > self.ANIMATION_TIME* 4:
            self.img = self.IMGS[0]
            self.img_count = 0
        
        if self.tilt <= -80:
            self.img = self.IMGS[1]
            self.img_count = self.ANIMATION_TIME * 2
        
        rotated_image = pygame.transform.rotate(self.img, self.tilt)

        #this rotates the image around it's center
        new_rectangle = rotated_image.get_rect(center=self.img.get_rect(topleft = (self.x, self.y)).center)

        win.blit(rotated_image, new_rectangle.topleft)

    def get_mask(self):
        return pygame.mask.from_surface(self.img)