from pygame import *
from random import randint
font.init()
w,h = 800,600
speed_x = 3
speed_y = 3

font1 = font.Font(None, 35)
lose1 = font1.render('PLAYER 1 LOSE!', True, (180, 0, 0))

lose2 = font1.render('PLAYER 2 LOSE!', True, (180, 0, 0))


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed

    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed

window = display.set_mode((w,h))

bg = transform.scale(image.load("won.jpg"), (w,h))

ball = GameSprite("ball.png", 50, 350, 10)
player1 = GameSprite("player1.png", 50, 350, 10)






finish = False
game = True
while game:
    if finish != True:
        window.blit(bg, (0,0))
        ball.rect.x += speed_x
        ball.rect.y += speed_y
    
        if ball.rect.y > h - 50\
            or ball.rect.y < 0:
                speed_y *= -1
        if ball.rect.x > w - 50\
            or ball.rect.x < 0:
                speed_x *= -1
        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))
        ball.reset()
    display.update()
