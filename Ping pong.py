import pygame as pg

from random import randint

class Base_sprite(pg.sprite.Sprite):
    def __init__(self, pic, x, y, w, h, speed):
        super().__init__()
        self.picture = pg.transform.scale(pg.image.load(pic), (w, h))
        self.rect = self.picture.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.image = self.picture
        self.speed = speed

    def draw(self):
        mw.blit(self.picture, (self.rect.x, self.rect.y))

class Rocket(Base_sprite):
    
    def update_l(self):
        keys = pg.key.get_pressed()

        if (keys[pg.K_w]) and self.rect.y >= 5:
            self.rect.y -= self.speed

        if (keys[pg.K_s]) and self.rect.y <= win_h - (self.rect.width + 40):
            self.rect.y += self.speed

    
    def update_r(self):
        keys = pg.key.get_pressed()

        if (keys[pg.K_UP]) and self.rect.y >= 5:
            self.rect.y -= self.speed

        if (keys[pg.K_DOWN]) and self.rect.y <= win_h - (self.rect.width + 40):
            self.rect.y += self.speed

class Ball(Base_sprite): 

    def update(self):
        # self.rect.y >= win_h - 5 or self.rect.y <= win_h + 5:
            #self.rect.y *= -1
            pass
 


win_w = 700    
win_h = 500

mw = pg.display.set_mode((win_w, win_h)) 
pg.display.set_caption('Ping pong')
clock = pg.time.Clock()

fon = pg.transform.scale(pg.image.load('fon.jpg'), (win_w, win_h))

rocket1 = Rocket('ping_rocket1.png', 30, 200, 25, 100, 4)
rocket2 = Rocket('ping_rocket2.png', 640, 200, 25, 100, 4)

ball = Ball('ball.png', 325, 230, 50, 50, 5)

play = True
while play:

    for e in pg.event.get():
        if e.type == pg.QUIT or \
                (e.type == pg.KEYDOWN and e.key == pg.K_ESCAPE):
            play = False 

   
    mw.blit(fon, (0,0))

    rocket1.update_l()
    rocket2.update_r()

    ball.update()

    rocket1.draw()
    rocket2.draw()

    ball.draw()


    pg.display.update()
    clock.tick(60)