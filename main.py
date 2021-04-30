from pygame import *
from random import randint

w,h = 800,600

window = display.set_mode((w,h))

bg = transform.scale(image.load("won.jpg"), (w,h))

def update_l(self):
    keys = key.get_pressed()
    if keys[K_w] and self.rect.y > 5:
        self.rect.y -= self.speed

def update_r(self):
    keys = key.get_pressed()
    if keys[K_UP] and self.rect.y > 5:
        self.rect.y -= self.speed

game = True
while game:
    window.blit(bg, (0,0))
    display.update()